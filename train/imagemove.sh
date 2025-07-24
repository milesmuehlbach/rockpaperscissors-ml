#!/bin/bash

# Prompt user for inputs
read -rp "Enter the input folder path: " input_folder
read -rp "Enter the output folder path: " output_folder
read -rp "Enter the fraction of images to copy (between 0 and 1): " fraction

# Validate inputs
if [[ ! -d "$input_folder" ]]; then
  echo "Input folder does not exist."
  exit 1
fi

if ! [[ "$fraction" =~ ^0\.[0-9]+$ || "$fraction" == "1" ]]; then
  echo "Fraction must be a number between 0 and 1 (exclusive or 1)."
  exit 1
fi

# Get list of image files (adjust extensions if needed)
mapfile -t image_files < <(find "$input_folder" -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.gif" -o -iname "*.bmp" \))

total_files=${#image_files[@]}
num_to_select=$(printf "%.0f" "$(echo "$total_files * $fraction" | bc)")

echo "Found $total_files images. Selecting $num_to_select at random..."

# Shuffle and pick random files
shuffled=($(printf "%s\n" "${image_files[@]}" | shuf -n "$num_to_select"))

# Copy files, preserving relative paths
for src_file in "${shuffled[@]}"; do
  rel_path="${src_file#$input_folder/}"
  dest_file="$output_folder/$rel_path"
  dest_dir=$(dirname "$dest_file")
  
  mkdir -p "$dest_dir"
  cp "$src_file" "$dest_file"
done

echo "Done. Copied $num_to_select images to $output_folder."
