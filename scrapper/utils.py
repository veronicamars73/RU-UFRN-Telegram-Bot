def get_text_in_li(li):
  anchors = li.find_all("a")
  elements = []
  for a in anchors:
    elements.append(a.text.strip())
  return elements