class VideoContractSimulator:
    def __init__(self):
        self.videos = {}

    def store_video_hash(self, user, ipfs_hash):
        self.videos[user] = ipfs_hash
        print(f"Stored {ipfs_hash} for {user}")

    def get_video_hash(self, user):
        return self.videos.get(user, None)

# Example usage
if __name__ == "__main__":
    contract = VideoContractSimulator()
    user_address = "user_mattral"  # Simulate an Ethereum address
    ipfs_hash = "f8bdddde64a497dd082f2be9b1ee43c03b63bfe7a68771ca74647595c90ec8a9"

    # Store a video hash
    contract.store_video_hash(user_address, ipfs_hash)

    # Retrieve a video hash
    retrieved_hash = contract.get_video_hash(user_address)
    print(f"Retrieved IPFS hash for {user_address}: {retrieved_hash}")
