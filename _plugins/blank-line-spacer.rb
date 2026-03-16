# Converts multiple blank lines in Markdown to reading-spacer divs,
# so spacing in the source is reflected on the frontend.
# 2 blank lines -> 1 spacer, 3 blank lines -> 2 spacers, etc.
Jekyll::Hooks.register [:documents, :pages], :pre_render do |doc|
  next unless doc.respond_to?(:content) && doc.content
  doc.content = doc.content.gsub(/\n{3,}/) do |match|
    extra = match.size - 2  # number of "extra" blank lines beyond the first
    spacers = extra.times.map { '<div class="reading-spacer"></div>' }.join("\n")
    "\n\n#{spacers}\n\n"
  end
end
