{ pkgs ? (let lock = builtins.fromJSON (builtins.readFile ./flake.lock);
in import (builtins.fetchTarball {
  url =
    "https://github.com/NixOS/nixpkgs/archive/${lock.nodes.nixpkgs.locked.rev}.tar.gz";
  sha256 = lock.nodes.nixpkgs.locked.narHash;
}) { }) }:

pkgs.mkShell {
  name = "character-vault-devshell";
  buildInputs = with pkgs; [
    python39
    python39Packages.virtualenv
  ];
  shellHook = ''
    export VIRTUAL_ENV=.venv
    export PATH="$VIRTUAL_ENV/bin:$PATH"
    if [ ! -d "$VIRTUAL_ENV" ]; then
      python -m venv $VIRTUAL_ENV
      source $VIRTUAL_ENV/bin/activate
      pip install -r requirements.txt
    else
      source $VIRTUAL_ENV/bin/activate
      pip install -r requirements.txt
    fi
  '';
}
