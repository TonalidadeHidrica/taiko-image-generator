use magick_rust::{magick_wand_genesis, MagickWand};

fn main() -> Result<(), &str>{
    magick_wand_genesis();
    let wand = MagickWand::new();
    wand.set_size(1920, 1080)?;
    wand.read_image("xc:transparent")?;
    wand.write_image("result.png")?;
    Ok(())
}
