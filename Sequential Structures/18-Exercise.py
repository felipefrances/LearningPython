"""Create a program that asks for the size of a file for download (in MB) and the speed of an Internet link (in Mbps),
calculate and provide the estimated download time for the file using this link (in minutes)."""

# Get input from the user
fileSizeMB = float(input("Please enter the size of the file for download (in MB): "))
linkSpeedMbps = float(input("Please enter the speed of the Internet link (in Mbps): "))

# Convert file size from MB to megabits
fileSizeMbps = fileSizeMB * 8

# Calculate download time (in seconds)
downloadTimeSeconds = fileSizeMbps / linkSpeedMbps

# Convert download time from seconds to minutes
downloadTimeMinutes = downloadTimeSeconds / 60

# Display the estimated download time
print("The estimated download time is approximately", round(downloadTimeMinutes, 2), "minutes.")





