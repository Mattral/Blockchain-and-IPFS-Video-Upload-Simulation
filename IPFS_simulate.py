import ipfshttpclient
import hashlib

# Function to simulate uploading to IPFS and getting a hash
def upload_to_ipfs(file_path):
    # Simulate an IPFS hash using SHA-256 for demo purposes
    # In a real scenario, you would upload the file to IPFS and get the CID
    with open(file_path, "rb") as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()
        return f"simulated_ipfs_hash_{file_hash}"

# Example usage
if __name__ == "__main__":
    file_path = "demo.mp4"
    ipfs_hash = upload_to_ipfs(file_path)
    print(f"File uploaded to IPFS with hash: {ipfs_hash}")
