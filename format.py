markup = """
<!doctype html>
<html>
    <head>
        <title>{0}</title>
    </head>

    <body>
        <h1>{1}</h1>
        <-- You can reuse an index in multiple places -->
        <h2>{1}</h2>
    </body>
</html>
"""

markup = markup.format ('My Title', 'Page Heading')
print (markup)

# can also use name place holders instead of index

# markup = """
# <!doctype html>
# <html>
#     <head>
#         <title>{title}</title>
#     </head>

#     <body>
#         <h1>{heading}</h1>
#     </body>
# </html>
# """

# markup = markup.format (title = 'My Title', heading = 'Page Heading')
# print (markup)