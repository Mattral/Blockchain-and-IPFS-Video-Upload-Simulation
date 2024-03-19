import streamlit as st
import hashlib

# Mock functions to simulate blockchain and IPFS interactions
def simulate_ipfs_upload(video_bytes):
    # This function would actually interact with IPFS in a real scenario
    # Here, it simply returns a simulated hash of the video bytes
    return hashlib.sha256(video_bytes).hexdigest()

def simulate_blockchain_store(hash_value):
    # This would interact with a blockchain to store the hash
    # For simulation, we just return the hash pretending it's stored
    return hash_value

def verify_video(video_bytes, expected_hash):
    # Simulate verification by hashing the video and comparing it to the expected hash
    return hashlib.sha256(video_bytes).hexdigest() == expected_hash

# Streamlit UI
st.title("Blockchain Video Hashing and Verification")

uploaded_file = st.file_uploader("Upload a video to hash and verify", type=["mp4"])

if uploaded_file is not None:
    # Read the uploaded video file
    video_bytes = uploaded_file.read()
    
    # Simulate IPFS upload to get a hash
    video_hash = simulate_ipfs_upload(video_bytes)
    st.success(f"Video hash (simulated IPFS CID): `{video_hash}`")
    
    # Simulate storing the hash on the blockchain
    blockchain_response = simulate_blockchain_store(video_hash)
    st.success(f"Hash stored on blockchain (simulated): `{blockchain_response}`")
    
    # Verification section (optional step for user)
    if st.button("Verify Video"):
        # In a real app, you'd fetch the expected hash from a blockchain
        expected_hash = blockchain_response  # Using the same hash for simulation purposes
        is_verified = verify_video(video_bytes, expected_hash)
        
        if is_verified:
            st.success("The video is verified successfully!")
        else:
            st.error("Verification failed. The video has been altered.")

