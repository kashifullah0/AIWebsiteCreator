html_code = """
<!DOCTYPE html>
<html>
<head>
  <title>My Preview</title>
</head>
<body>
  <h1>Hello from Python!</h1>
</body>
</html>
"""

with open("preview.html", "w") as f:
    f.write(html_code)

import webbrowser
webbrowser.open("preview.html")
