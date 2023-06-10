// Function to handle the file selection
function handleFileSelection() {
    // Get the selected file input element
    const fileInput = document.getElementById("property-image");

    // Get the selected file
    const file = fileInput.files[0];

    // Get the file extension
    const fileExtension = file ? getFileExtension(file.name) : "";

    // Define the allowed file extensions
    const allowedExtensions = ["jpg", "jpeg", "png"];

    // Define the maximum file size in bytes (2 MB)
    const maxSize = 2 * 1024 * 1024;

    // Get the error message element
    const fileError = document.getElementById("fileError");

    // Check if a file is selected
    if (file) {
        // Check if the file extension is allowed
        if (allowedExtensions.includes(fileExtension.toLowerCase())) {
            // Check if the file size is within the allowed limit
            if (file.size <= maxSize) {
                // Update the selected file name display
                document.getElementById("noFile").textContent = file.name;

                // Clear the error message
                fileError.textContent = "";
            } else {
                // Clear the file input value
                fileInput.value = "";

                // Update the selected file name display
                document.getElementById("noFile").textContent = "No file chosen...";

                // Set the error message
                fileError.textContent = "Please choose a file with a maximum size of 2 MB.";
            }
        } else {
            // Clear the file input value
            fileInput.value = "";

            // Update the selected file name display
            document.getElementById("noFile").textContent = "No file chosen...";

            // Set the error message
            fileError.textContent = "Please choose a file with a valid image extension (jpg, jpeg, png).";
        }
    } else {
        // No file selected, clear the file name display
        document.getElementById("noFile").textContent = "No file chosen...";

        // Clear the error message
        fileError.textContent = "";
    }
}

// Function to get the file extension
function getFileExtension(filename) {
    return filename.split(".").pop();
}

