const express = require('express');
const path = require('path');
const fs = require('fs');
const { execSync } = require('child_process');

const app = express();
const PORT = 3456;
const ROOT = path.join(__dirname, '..');
const POSTS_DIR = path.join(ROOT, '_posts');

app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

function slugify(title) {
  return title
    .toLowerCase()
    .replace(/[^\w\u4e00-\u9fa5\s-]/g, '')
    .replace(/\s+/g, '-')
    .replace(/-+/g, '-')
    .trim();
}

function getDateStr() {
  const d = new Date();
  return d.toISOString().slice(0, 10);
}

app.post('/api/post', (req, res) => {
  const { title, content, category, excerpt } = req.body;
  if (!title || !content) {
    return res.status(400).json({ error: '标题和正文不能为空' });
  }

  const date = getDateStr();
  const slug = slugify(title) || 'untitled';
  const filename = `${date}-${slug}.md`;

  const frontMatter = [
    '---',
    `layout: post`,
    `title: "${(title || '').replace(/"/g, '\\"')}"`,
    `date: ${date}`,
    `category: ${category || 'Writing'}`,
    ...(excerpt ? [`excerpt: "${(excerpt || '').replace(/"/g, '\\"')}"`] : []),
    '---',
    '',
    content.trim(),
    ''
  ].join('\n');

  const filepath = path.join(POSTS_DIR, filename);
  fs.writeFileSync(filepath, frontMatter, 'utf8');

  res.json({ success: true, filename, path: filepath });
});

app.post('/api/publish', (req, res) => {
  const { filename, title } = req.body;
  if (!filename) return res.status(400).json({ error: '缺少文件名' });

  try {
    execSync(`git add _posts/${filename}`, { cwd: ROOT });
    execSync(`git commit -m "Add post: ${title || filename}"`, { cwd: ROOT });
    execSync('git push origin main', { cwd: ROOT });
    res.json({ success: true });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.listen(PORT, () => {
  console.log(`\n  博客编辑器已启动 → http://localhost:${PORT}\n`);
});
