"""Start Alobo in the current Terminal and open the default browser."""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import threading
import webbrowser

ROOT = Path(__file__).resolve().parent

def main():
    parser = argparse.ArgumentParser(description='Chay web Alobo cho Selenium IDE')
    parser.add_argument('--port', type=int, default=8000, help='Cong web, mac dinh 8000')
    parser.add_argument('--no-browser', action='store_true', help='Khong tu mo trinh duyet')
    args = parser.parse_args()
    if not 0 <= args.port <= 65535:
        parser.error('Cong phai tu 0 den 65535')
    if not (ROOT / 'index.html').is_file():
        print('Khong tim thay index.html. Hay giai nen toan bo thu muc.')
        return 1
    handler = partial(SimpleHTTPRequestHandler, directory=str(ROOT))
    try:
        server = ThreadingHTTPServer(('127.0.0.1', args.port), handler)
    except OSError as exc:
        print(f'Khong mo duoc cong {args.port}: {exc}')
        print('Dung server cu bang Ctrl+C, hoac chay: python run_web.py --port 8080')
        print('Neu doi cong, hay doi Base URL trong Selenium IDE cho khop.')
        return 1
    url = f'http://localhost:{server.server_port}/'
    print('ALOBO DA SAN SANG: ' + url, flush=True)
    print('Selenium IDE Base URL: ' + url, flush=True)
    print('Giu Terminal nay mo. Nhan Ctrl+C de dung server.', flush=True)
    if not args.no_browser:
        opener = threading.Timer(0.4, lambda: webbrowser.open(url))
        opener.daemon = True
        opener.start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nDa dung web Alobo.')
    finally:
        server.server_close()
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
