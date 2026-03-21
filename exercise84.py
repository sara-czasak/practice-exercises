import pyglet

window = pyglet.window.Window()

label = pyglet.text.Label(
    'Hello World!',
    font_size=60,
    x=window.width / 3.5,
    y=window.height / 2,
    )

label.draw()

pyglet.app.run()