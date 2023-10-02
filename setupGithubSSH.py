import os, stat, time
from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from codecs import decode

KEY_NAME_PREFIX = 'github'
PRIVATE_KEY_NAME = KEY_NAME_PREFIX + '_ed25519'
PUBLIC_KEY_NAME = PRIVATE_KEY_NAME + '.pub'
DEFAULT_KEY_DIRECTORY_PATH = os.path.expanduser('~') + '/.ssh'
PRIVATE_KEY_PATH = DEFAULT_KEY_DIRECTORY_PATH + '/' + PRIVATE_KEY_NAME
PUBLIC_KEY_PATH = DEFAULT_KEY_DIRECTORY_PATH + '/' + PUBLIC_KEY_NAME

def generate_ssh_private_key():
    return Ed25519PrivateKey.generate()

def write_ssh_key_pair(private_key):
    private_bytes = private_key.private_bytes(
        encoding=crypto_serialization.Encoding.PEM,
        format=crypto_serialization.PrivateFormat.OpenSSH,
        encryption_algorithm = crypto_serialization.NoEncryption()
    )
    public_bytes = private_key.public_key().public_bytes(
        crypto_serialization.Encoding.OpenSSH,
        crypto_serialization.PublicFormat.OpenSSH,
    )

    with open(PRIVATE_KEY_PATH, 'wb') as private_key_file:
        private_key_file.write(private_bytes)
    with open(PUBLIC_KEY_PATH, 'wb') as public_key_file:
        public_key_file.write(public_bytes)
    os.chmod(PRIVATE_KEY_PATH, stat.S_IRWXU)
    os.chmod(PUBLIC_KEY_PATH, stat.S_IRWXU)

def display_public_key(private_key):
    public_bytes = private_key.public_key().public_bytes(
        crypto_serialization.Encoding.OpenSSH,
        crypto_serialization.PublicFormat.OpenSSH
    )
    print(decode(public_bytes))

def add_key_to_ssh_agent(private_key_path):
    # TODO: Debug why this is not actually working in the script. Needs to be run manually right now
    os.system('eval "$(ssh-agent -s)"')
    time.sleep(1)
    os.system('ssh-add ' + private_key_path)


def main():
    # Check for existing script SSH key default SSH folder
    with os.scandir(DEFAULT_KEY_DIRECTORY_PATH) as sshDir:
        keyMatches = list(filter(lambda itr: PRIVATE_KEY_NAME in itr.path, sshDir))
    if not keyMatches:
        # TODO: Add logic to present an option for displaying the existing key
        print('Keys not found, generating...')
        private_key = generate_ssh_private_key()
        write_ssh_key_pair(private_key)
        display_public_key(private_key)
    add_key_to_ssh_agent(PRIVATE_KEY_PATH)

main()

