
from compression_api import compress_image_file
from reconstruction_api import reconstruct_image_from_file
from benchmark import benchmark_image


def main():
    """Demo of the quad tree compression system"""
    
    # Example: Compress an image
    input_image = "input/branch.jpg"  # Replace with your image path
    compressed_file = "output/compressed.qid"
    reconstructed_file = "output/com_branch.jpg"
    
    try:
        # Compress the image
        print("Compressing image...")
        compress_image_file(input_image, compressed_file, iterations=10000)
        print(f"Image compressed and saved to {compressed_file}")
        
        # Reconstruct the image
        print("Reconstructing image...")
        reconstructed_image = reconstruct_image_from_file(compressed_file)
        reconstructed_image.save(reconstructed_file)
        print(f"Image reconstructed and saved to {reconstructed_file}")
        
        # Run benchmark
        print("\nRunning benchmark...")
        benchmark_image(input_image, 10000, compressed_file)
        
    except FileNotFoundError:
        print(f"Image file {input_image} not found. Please provide a valid image path.")
        print("You can test with any image by updating the input_image variable.")


if __name__ == "__main__":
    main()
