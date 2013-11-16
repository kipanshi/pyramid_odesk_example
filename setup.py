from setuptools import setup

requires = [
    'pyramid',
    'pyramid_jinja2',
    'pyramid_odesk',
    'pyramid_debugtoolbar'
]

setup(
    name='pyramid_odesk_example',
    version='1.0',
    install_requires=requires,
    entry_points="""\
    [paste.app_factory]
    main = pyramid_odesk_example:main
    """,
)
