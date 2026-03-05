#!/usr/bin/env ruby
# Generates /en/ versions of posts for language-specific Open Graph meta.
# Run before Jekyll build. Creates en/writing/... and en/research/... pages.

require 'yaml'
require 'fileutils'
require 'date'

POSTS_DIR = '_posts'
OUT_BASE = 'en'

Dir.glob(File.join(POSTS_DIR, '*.md')).each do |path|
  content = File.read(path)
  next unless content.start_with?('---')
  _, fm, body = content.split('---', 3)
  data = YAML.load(fm, permitted_classes: [Date, Time])
  next unless data && data['title_en']

  date_str = data['date'].to_s
  date = Date.parse(date_str)
  slug = File.basename(path, '.md').sub(/^\d{4}-\d{2}-\d{2}-/, '')
  cat = (data['category'] || 'Writing').downcase
  year = date.strftime('%Y')
  month = date.strftime('%m')
  day = date.strftime('%d')

  out_dir = File.join(OUT_BASE, cat, year, month, day)
  FileUtils.mkdir_p(out_dir)
  out_path = File.join(out_dir, "#{slug}.md")

  en_fm = {
    'layout' => 'post',
    'title' => data['title_en'],
    'title_en' => data['title_en'],
    'title_zh' => data['title'],
    'excerpt' => data['excerpt_en'] || data['excerpt'],
    'excerpt_en' => data['excerpt_en'],
    'excerpt_zh' => data['excerpt'],
    'date' => date_str,
    'category' => data['category'],
    'image' => data['image'],
    'cover' => data['cover'],
    'permalink' => "/en/#{cat}/#{year}/#{month}/#{day}/#{slug}.html"
  }
  en_fm['author'] = data['author'] if data['author']

  File.write(out_path, en_fm.to_yaml + "---\n" + body)
  puts "Generated #{out_path}"
end
