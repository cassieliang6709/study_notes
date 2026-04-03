"""
Unit tests for assignment6_complete.py
Run with:  python3 test_assignment6.py
"""
import sys, types, numpy as np, tensorflow as tf

# ── mock load_data so the module imports without the real file ──────────────
mock_mod = types.ModuleType("load_data")
mock_mod.load_data = lambda path: []
sys.modules["load_data"] = mock_mod

# patch pandas too (imported but unused in our functions)
sys.modules.setdefault("pandas", types.ModuleType("pandas"))

import importlib
a6 = importlib.import_module("assignment6_complete")

PASS = "\033[92mPASS\033[0m"
FAIL = "\033[91mFAIL\033[0m"

def check(name, cond, detail=""):
    status = PASS if cond else FAIL
    print(f"  [{status}] {name}" + (f"  — {detail}" if detail else ""))
    return cond

results = []

# ════════════════════════════════════════════════════════════════════════════
print("\n── Q1: get_sentence_vectorizer ─────────────────────────────────────")
sentences = [
    "Peter lives in New York",
    "Alice works at Google",
    "Bob visited Paris last summer",
]
sv, vocab = a6.get_sentence_vectorizer(sentences)

results += [
    check("returns TextVectorization layer",
          isinstance(sv, tf.keras.layers.TextVectorization)),
    check("vocab is a list", isinstance(vocab, list)),
    check("vocab is non-empty", len(vocab) > 0,
          f"len={len(vocab)}"),
    check("known word in vocab", "Peter" in vocab or "peter" in vocab,
          f"sample vocab={vocab[:8]}"),
    check("vectorizer produces int tensor",
          sv(["hello world"]).dtype in (tf.int32, tf.int64)),
]

# ════════════════════════════════════════════════════════════════════════════
print("\n── Q2: label_vectorizer ────────────────────────────────────────────")
tag_map = {"O": 0, "B-per": 1, "I-per": 2, "B-geo": 3, "I-geo": 4}
labels  = ["B-per O B-geo", "O O", "B-per I-per O O O"]
out = a6.label_vectorizer(labels, tag_map)

results += [
    check("output is ndarray", isinstance(out, np.ndarray)),
    check("2-D output", out.ndim == 2,
          f"shape={out.shape}"),
    check("all rows same length (padded)",
          len(set(len(row) for row in out)) == 1),
    check("first row correct IDs",
          list(out[0, :3]) == [1, 0, 3],          # B-per O B-geo
          f"got {list(out[0])}"),
    check("padding fills with 0",
          out[1, 2] == 0,                          # 'O O' → [0,0,pad,pad,pad]
          f"row1={list(out[1])}"),
    check("longest row has no padding",
          out[2, 4] == 0,                          # last real token is index 4
          f"row2={list(out[2])}"),
]

# ════════════════════════════════════════════════════════════════════════════
print("\n── Q3.1: NER model architecture ────────────────────────────────────")
len_tags, vocab_size, emb_dim = 5, 100, 16
model = a6.NER(len_tags, vocab_size, embedding_dim=emb_dim)

layer_types = [type(l).__name__ for l in model.layers]
results += [
    check("is Sequential", isinstance(model, tf.keras.Sequential)),
    check("3 layers", len(model.layers) == 3,
          f"layers={layer_types}"),
    check("first layer is Embedding", layer_types[0] == "Embedding"),
    check("second layer is LSTM",     layer_types[1] == "LSTM"),
    check("third layer is Dense",     layer_types[2] == "Dense"),
    check("Embedding masks zero",     model.layers[0].mask_zero),
    check("LSTM returns sequences",   model.layers[1].return_sequences),
    check("Dense output units == len_tags",
          model.layers[2].units == len_tags,
          f"got {model.layers[2].units}"),
]
# forward-pass shape check
dummy = tf.zeros((2, 10), dtype=tf.int32)
out_shape = model(dummy).shape
results += [
    check("output shape (batch, seq, tags)",
          tuple(out_shape) == (2, 10, len_tags),
          f"got {tuple(out_shape)}"),
]

# ════════════════════════════════════════════════════════════════════════════
print("\n── Q3.2: masked_loss ───────────────────────────────────────────────")
B, S, C = 2, 5, 4
# y_true: last position of each row is padding (0)
y_true_loss = tf.constant([[1, 2, 3, 1, 0],
                            [2, 1, 0, 0, 0]], dtype=tf.int32)
# uniform log-softmax predictions
y_pred_loss = tf.fill([B, S, C], np.float32(-np.log(C)))   # uniform → loss = log(C)

loss_val = a6.masked_loss(y_true_loss, y_pred_loss).numpy()
expected = np.log(C)

# All-padding batch → should not crash (denominator clamp)
y_true_allpad = tf.zeros((2, 5), dtype=tf.int32)
loss_allpad = a6.masked_loss(y_true_allpad, y_pred_loss).numpy()

results += [
    check("returns scalar", np.isscalar(loss_val) or loss_val.ndim == 0),
    check("loss ≈ log(C) for uniform preds",
          abs(loss_val - expected) < 0.05,
          f"got {loss_val:.4f}, expected ≈ {expected:.4f}"),
    check("all-padding batch doesn't crash / nan",
          not np.isnan(loss_allpad), f"got {loss_allpad}"),
    # Use actual log-softmax style values (model output), not raw logits
    # log_softmax([0, 500, 0, 0]) ≈ [-500, 0, -500, -500]  → strong class-1 prediction
    check("perfect predictions → low loss", (lambda:
        a6.masked_loss(
            tf.constant([[1, 2], [2, 1]]),
            tf.nn.log_softmax(tf.constant(
                [[[0, 500, 0, 0], [0, 0, 500, 0]],   # correct: class 1 then class 2
                 [[0, 0, 500, 0], [0, 500, 0, 0]]],  # correct: class 2 then class 1
                dtype=tf.float32), axis=-1)
        ).numpy() < 0.01)()),
]

# ════════════════════════════════════════════════════════════════════════════
print("\n── Q3.3: masked_accuracy ───────────────────────────────────────────")
# y_pred shaped (batch, seq, classes) — argmax at dim -1 gives predicted class
# Build y_pred so that argmax matches y_true exactly for non-pad positions
y_true_acc = tf.constant([[1, 2, 0],     # class 1, class 2, PADDING
                           [3, 0, 0]], dtype=tf.int32)   # class 3, PADDING, PADDING
# One-hot-like: correct class gets 1.0, others 0.0
def onehot_pred(y_true_np, C=5):
    out = np.full((*y_true_np.shape, C), -10.0, dtype=np.float32)
    for i in range(y_true_np.shape[0]):
        for j in range(y_true_np.shape[1]):
            c = y_true_np[i, j]
            out[i, j, c] = 10.0   # includes padding class 0 for pad positions
    return tf.constant(out)

y_pred_correct = onehot_pred(y_true_acc.numpy())
acc_perfect = a6.masked_accuracy(y_true_acc, y_pred_correct).numpy()

# Wrong predictions for real tokens, correct for padding
y_pred_wrong = np.full((2, 3, 5), -10.0, dtype=np.float32)
y_pred_wrong[:, :, 4] = 10.0   # always predict class 4 (never 0)
y_pred_wrong = tf.constant(y_pred_wrong)
acc_wrong = a6.masked_accuracy(y_true_acc, y_pred_wrong).numpy()

results += [
    check("perfect preds → accuracy == 1.0",
          abs(acc_perfect - 1.0) < 1e-5, f"got {acc_perfect:.4f}"),
    check("fully wrong preds → accuracy == 0.0",
          abs(acc_wrong - 0.0) < 1e-5,   f"got {acc_wrong:.4f}"),
]

# Partial accuracy: 1 out of 3 real tokens correct
y_true_partial = tf.constant([[1, 2, 3, 0]], dtype=tf.int32)   # 3 real, 1 pad
y_pred_partial = np.full((1, 4, 5), -10.0, dtype=np.float32)
y_pred_partial[0, 0, 1] = 10.0   # token 0 correct  (class 1)
y_pred_partial[0, 1, 4] = 10.0   # token 1 wrong    (class 4 ≠ 2)
y_pred_partial[0, 2, 4] = 10.0   # token 2 wrong    (class 4 ≠ 3)
y_pred_partial[0, 3, 0] = 10.0   # padding position — must be ignored
acc_partial = a6.masked_accuracy(y_true_partial,
                                  tf.constant(y_pred_partial)).numpy()
results += [
    check("1/3 correct → accuracy ≈ 0.333",
          abs(acc_partial - 1/3) < 1e-4, f"got {acc_partial:.4f}"),
]

# ════════════════════════════════════════════════════════════════════════════
print("\n── Q4: predict ─────────────────────────────────────────────────────")
# Train a tiny model for a few steps so predict() returns something sensible
tiny_tags   = {"O": 0, "B-per": 1, "I-per": 2}
tiny_sents  = ["Alice and Bob", "Bob went home"]
tiny_labels = ["B-per O B-per", "B-per O O"]

sv2, vocab2 = a6.get_sentence_vectorizer(tiny_sents)
model2 = a6.NER(len(tiny_tags), len(vocab2), embedding_dim=8)
model2.compile(optimizer="adam", loss=a6.masked_loss, metrics=[a6.masked_accuracy])

ds = a6.generate_dataset(tiny_sents, tiny_labels, sv2, tiny_tags)
model2.fit(ds.batch(2), epochs=3, verbose=0)

preds = a6.predict("Alice and Bob", model2, sv2, tiny_tags)
results += [
    check("predict returns a list", isinstance(preds, list)),
    check("one prediction per token",
          len(preds) == len("Alice and Bob".split()),
          f"len(preds)={len(preds)}, tokens={len('Alice and Bob'.split())}"),
    check("predictions are valid tags",
          all(p in tiny_tags for p in preds),
          f"got {preds}"),
]

# ════════════════════════════════════════════════════════════════════════════
total = len(results)
passed = sum(results)
print(f"\n{'═'*60}")
print(f"Result: {passed}/{total} tests passed", "✓" if passed == total else "✗")
if passed < total:
    sys.exit(1)
