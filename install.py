"""Install the paramiko dependency the VPS Manager daemon needs.

fused-render installs paramiko on its own from this folder's pyproject.toml,
so this is only for running vps.py under some other interpreter. paramiko is
the only third-party package the daemon imports — the HTTP server and the
terminal's WebSocket are standard library.

    python install.py
"""
import subprocess
import sys


def main():
    try:
        import paramiko
        have = tuple(int(n) for n in paramiko.__version__.split(".")[:2]
                     if n.isdigit())
        if have >= (3, 2):
            print(f"paramiko {paramiko.__version__} already installed "
                  f"for {sys.executable}")
            return
        print(f"paramiko {paramiko.__version__} is too old — "
              f"PKey.from_path() arrived in 3.2")
    except ImportError:
        pass
    print(f"installing paramiko into {sys.executable} …")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-U",
                           "paramiko>=3.2"])
    print("done — open index.html in fused-render")


if __name__ == "__main__":
    main()
