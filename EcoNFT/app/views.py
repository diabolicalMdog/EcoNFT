from app import app
from flask import request
from flask import render_template
import arrow
import zlib

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template("index.html", body_content="NFTs will never be the same, and nature will heal!")
    else:
        nft_in = request.form["nft_input"]
        nft_recip = request.form["recipient"]
        satoshi_epoch_0 = arrow.get('2009-01-03T00:00:00.000000+00:00')
        satoshi_epoch_now = arrow.utcnow() - satoshi_epoch_0

        yamlt_object = f"econft\n\ttime:\t{satoshi_epoch_now}\n\tsignature:\t{zlib.crc32(nft_in.encode('utf-8') + nft_recip.encode('utf-8'))}"
        return render_template("final.html", nft_recip=nft_recip, yamlt_object=yamlt_object)
