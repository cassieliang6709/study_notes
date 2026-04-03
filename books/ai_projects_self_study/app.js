const allowedDocs = new Set([
  'README.md',
  'track_1_rag_systems.md',
  'track_2_llm_from_scratch.md',
  'track_3_alignment_and_agent_rl.md',
  'project_rag_from_scratch.md',
  'project_complex_rag_guide.md',
  'project_rag_techniques.md',
  'project_deep_searcher.md',
  'project_minimind.md',
  'project_cs336.md',
  'project_model_alignment_from_scratch.md',
  'project_openpipe_art.md',
  'week_plan_rag_from_scratch.md',
  'week_plan_complex_rag_guide.md',
  'week_plan_rag_techniques.md',
  'week_plan_deep_searcher.md',
  'week_plan_minimind.md',
  'week_plan_cs336.md',
  'week_plan_model_alignment_from_scratch.md',
  'week_plan_openpipe_art.md',
  'self_test_rag.md',
  'self_test_llm_from_scratch.md',
  'self_test_alignment_agent_rl.md',
  'self_test_capstone.md',
  'answer_key_rag.md',
  'answer_key_llm_from_scratch.md',
  'answer_key_alignment_agent_rl.md',
  'answer_key_capstone.md',
]);

const params = new URLSearchParams(window.location.search);
const requestedDoc = params.get('doc');
const doc = allowedDocs.has(requestedDoc) ? requestedDoc : 'README.md';

const contentEl = document.getElementById('content');
const titleEl = document.getElementById('doc-title');
const rawLinkEl = document.getElementById('raw-link');

marked.setOptions({
  gfm: true,
  breaks: false,
});

function setActiveNav(docName) {
  document.querySelectorAll('.nav-group a').forEach((link) => {
    const href = link.getAttribute('href') || '';
    link.classList.toggle('active', href === `?doc=${docName}`);
  });
}

function rewriteRelativeMarkdownLinks(container) {
  container.querySelectorAll('a').forEach((link) => {
    const href = link.getAttribute('href');
    if (!href) return;

    if (href.startsWith('./') && href.endsWith('.md')) {
      const docName = href.replace('./', '');
      if (allowedDocs.has(docName)) {
        link.setAttribute('href', `?doc=${docName}`);
      }
    }
  });
}

async function loadDoc(docName) {
  try {
    const response = await fetch(`./${docName}`);
    if (!response.ok) {
      throw new Error(`Failed to load ${docName}`);
    }

    const markdown = await response.text();
    const html = marked.parse(markdown);
    contentEl.innerHTML = DOMPurify.sanitize(html);
    rewriteRelativeMarkdownLinks(contentEl);
    setActiveNav(docName);

    const firstHeading = contentEl.querySelector('h1');
    titleEl.textContent = firstHeading ? firstHeading.textContent : docName;
    rawLinkEl.href = `./${docName}`;
  } catch (error) {
    titleEl.textContent = 'Load Error';
    contentEl.innerHTML = `<p>无法加载文档：${docName}</p><pre>${error.message}</pre>`;
  }
}

loadDoc(doc);
