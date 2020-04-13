This repo is forked from [lepture/captcha](https://github.com/lepture/captcha)
Code is quick modified for my project. Re-structure is needed in the future.
Change is listed at the bottom

Captcha
=======

A captcha library that generates audio and image CAPTCHAs.

.. image:: https://img.shields.io/badge/donate-lepture-ff69b4.svg
   :target: https://lepture.com/donate
   :alt: Donate lepture
.. image:: https://img.shields.io/badge/I0-patreon-f96854.svg
   :target: https://patreon.com/lepture
   :alt: Become a Patreon
.. image:: https://travis-ci.org/lepture/captcha.svg?branch=master
   :target: https://travis-ci.org/lepture/captcha
.. image:: https://ci.appveyor.com/api/projects/status/amm21f13lx4wuura?svg=true
   :target: https://ci.appveyor.com/project/lepture/captcha
.. image:: https://coveralls.io/repos/lepture/captcha/badge.svg?branch=master
   :target: https://coveralls.io/r/lepture/captcha

Features
--------

1. Audio CAPTCHAs `DEMO <https://github.com/lepture/captcha/releases/download/v0.1-beta/out.wav>`_
2. Image CAPTCHAs

.. image:: https://cloud.githubusercontent.com/assets/290496/5213632/95e68768-764b-11e4-862f-d95a8f776cdd.png


Installation
------------

Install captcha with pip::

    $ git clone https://github.com/lentychang/captcha.git
    $ cd captcha && python3 setup.py install

Usage
-----

Audio and Image CAPTCHAs are in seprated modules:

.. code:: python

    from captcha.audio import AudioCaptcha
    from captcha.image import ImageCaptcha

    audio = AudioCaptcha(voicedir='/path/to/voices')
    image = ImageCaptcha(width=160, height=60, fonts=['/path/A.ttf', '/path/B.ttf'], font_sizes=[25,30,32])

    data = audio.generate('1234')
    audio.write('1234', 'out.wav')

    im = image.create_captcha_image(chars=f"{123:0>6d}",color=(255,0,0),background=(255,255,255))
    im = ImageCaptcha.create_noise_dots(im, color=(200,200,0))
    im = ImageCaptcha.create_noise_curve(im, color=(0,255,255))
    im.save("filename.png",format="png")

This is the APIs for your daily works. We do have built-in voice data and font
data. But it is suggested that you use your own voice and font data.


Change
------
- add enable_warping flag


TODO
----
- Add add_noise_line function
- Add filename member to class, so that write function can use for save file
- change static method to instance method, so that noise can be called directly?
