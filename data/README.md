# Dataset

Place the complete Rotten Tomatoes dataset in this directory using this exact filename:

`Rotten_Tomatoes_Movies3.csv`

Expected scale: approximately **16,639 movie records**.

The source data contains movie metadata, critic information, genres, people, studio information and the target `audience_rating`.

## Expected columns

The project was designed around fields including:

- `movie_title`
- `movie_info`
- `critics_consensus`
- `rating`
- `genre`
- `directors`
- `writers`
- `cast`
- `in_theaters_date`
- `on_streaming_date`
- `runtime_in_minutes`
- `studio_name`
- `tomatometer_status`
- `tomatometer_rating`
- `tomatometer_count`
- `audience_rating`

Do not commit the CSV blindly. Check its size first. If it is too large for normal Git hosting, use Git LFS or keep it outside the repository and document the download/source process.
