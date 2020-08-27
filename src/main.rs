use magick_rust::{magick_wand_genesis, MagickWand, DrawingWand, PixelWand};
use std::fs::create_dir_all;
use std::io;
use std::io::Error;
use std::path::Path;

#[derive(Debug)]
enum CustomError {
    IOError(io::Error),
    StrError(&'static str),
}

impl From<io::Error> for CustomError {
    fn from(error: Error) -> Self {
        Self::IOError(error)
    }
}

impl From<&'static str> for CustomError {
    fn from(error: &'static str) -> Self {
        Self::StrError(error)
    }
}

fn main() -> Result<(), CustomError> {
    let output_dir = Path::new("output");
    create_dir_all(output_dir)?;

    magick_wand_genesis();
    create_background(output_dir);
    Ok(())
}

fn create_background<P>(output_dir: P) -> Result<(), CustomError>
where
    P: AsRef<Path>,
{
    let wand = MagickWand::new();
    wand.set_size(1920, 1080)?;
    wand.read_image("xc:transparent")?;
    let mut drawing_wand = DrawingWand::new();
    drawing_wand.set_stroke_color("none");

    wand.write_image(
        output_dir
            .into()
            .join("test1.png")
            .to_str()
            .ok_or("File path not converted successfully")?,
    )?;
    Ok(())
}
