# Hero orb

`assets/hero.webp` is rendered from `index.html`, a three.js shader. To re-render it:

    mkdir -p frames && python3 server.py 8797          # serves this folder, saves POSTed frames
    open "http://localhost:8797/index.html?capture=1"  # renders 144 frames into frames/; title becomes "done"
    uv run --with pillow python encode.py ../../hero.webp 80

`index.html` on its own plays the loop live, and `?t=<seconds>` shows a single frame.
