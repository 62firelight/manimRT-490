from lazydocs import generate_docs

# The parameters of this function correspond to the CLI options
generate_docs(["manim_rt"], output_path="./docs", ignored_modules=["manim"], overview_file="overview", watermark=True, remove_package_prefix=True, src_base_url="..\\blob\main")