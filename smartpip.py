import sys
import subprocess
import os

def main():
  if len(sys.argv) < 3 or sys.argv[1] not in ["install", "uninstall"]:
    print("Usage: python smartpip.py [install|uninstall] <package-name>")
    sys.exit(1)

  action = sys.argv[1]
  package = sys.argv[2]

  try:
    # Install/uninstall
    if action == "install":
      subprocess.run([sys.executable, "-m", "pip", "install", package], check=True)
    else:
      subprocess.run([sys.executable, "-m", "pip", "uninstall", package, "-y"], check=True)

    # Save requirements.txt to CURRENT directory
    current_dir = os.getcwd()
    req_path = os.path.join(current_dir, "requirements.txt")
    
    with open(req_path, "w") as f:
      subprocess.run([sys.executable, "-m", "pip", "freeze"], stdout=f, check=True)

    print(f"✅ {package} {action}ed. requirements.txt created at:\n{req_path}")

  except subprocess.CalledProcessError as e:
    print(f"❌ Error: {e}")
    sys.exit(1)

if __name__ == "__main__":
  main()