import os, stat, time
from cryptography.hazmat.primitives import serialization as crypto_serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from codecs import decode

KEY_NAME_PREFIX = 'github'
PRIVATE_KEY_NAME = KEY_NAME_PREFIX + '_ed25519'
PUBLIC_KEY_NAME = PRIVATE_KEY_NAME + '.pub'

def generate_ssh_private_key():
    return Ed25519PrivateKey.generate()

def write_ssh_key_pair(private_key, key_directory_path):
    private_key_path = key_directory_path + '/' + PRIVATE_KEY_NAME
    public_key_path = key_directory_path + '/' + PUBLIC_KEY_NAME

    private_bytes = private_key.private_bytes(
        encoding=crypto_serialization.Encoding.PEM,
        format=crypto_serialization.PrivateFormat.OpenSSH,
        encryption_algorithm = crypto_serialization.NoEncryption()
    )
    public_bytes = private_key.public_key().public_bytes(
        crypto_serialization.Encoding.OpenSSH,
        crypto_serialization.PublicFormat.OpenSSH,
    )

    with open(private_key_path, 'wb') as private_key_file:
        private_key_file.write(private_bytes)
    with open(public_key_path, 'wb') as public_key_file:
        public_key_file.write(public_bytes)
    os.chmod(private_key_path, stat.S_IRWXU)
    os.chmod(public_key_path, stat.S_IRWXU)

def display_public_key(private_key):
    public_bytes = private_key.public_key().public_bytes(
        crypto_serialization.Encoding.OpenSSH,
        crypto_serialization.PublicFormat.OpenSSH
    )
    print(decode(public_bytes))

def add_key_to_ssh_agent(private_key_path):
    os.system('eval "$(ssh-agent -s)"')
    time.sleep(1)
    os.system('ssh-add ' + private_key_path)


def main():
    key_directory_path = os.path.expanduser('~') + '/.ssh'
    private_key_path = key_directory_path + '/' + PRIVATE_KEY_NAME
    # Check for existing script SSH key default SSH folder
    with os.scandir(key_directory_path) as sshDir:
        keyMatches = list(filter(lambda itr: PRIVATE_KEY_NAME in itr.path, sshDir))
    if keyMatches:
        # TODO: Add logic to present an option for displaying the existing key
        print('Keys found, exiting.')
        exit()

    private_key = generate_ssh_private_key()
    write_ssh_key_pair(private_key, key_directory_path)
    add_key_to_ssh_agent(private_key_path)
    display_public_key(private_key)
    
    

main()

