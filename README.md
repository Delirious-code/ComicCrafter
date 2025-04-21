# ComicCrafter

**ComicCrafter** is a Python-based tool designed to generate comic-style stories with the help of Large Language Models (LLMs) and image generation models like Stable Diffusion. The tool takes a narrative prompt, processes it into structured scenes with dialogue and descriptions, and generates corresponding images using **ComicDiffusion**. It's aimed at those looking for a creative way to automate the generation of comic-style content, from story creation to visual representation.

## Features

- **Story Generation**: ComicCrafter leverages the power of **Mistral** (or any chosen LLM) to automatically generate full-length stories. The LLM takes a user-provided prompt and crafts a narrative that includes characters, settings, and plot developments.
  
- **Scene Breakdown**: Once the story is generated, ComicCrafter breaks the narrative into individual scenes, each containing descriptions and dialogue. This helps in the structuring of the story in a comic-friendly format. The scenes are organized for easy translation into comic panels.

- **Dialogue and Descriptions**: The tool separates the dialogue from the descriptions within each scene, ensuring that both narrative components are clear and ready for further use, such as speech bubbles and background imagery.

- **Image Generation**: After structuring the story into scenes, ComicCrafter automatically generates corresponding comic-style images. **ComicDiffusion**, a specialized version of Stable Diffusion, is used to create the artwork for each scene based on the dialogue and scene descriptions. 

- **Organized Folder Output**: The entire output—stories, scenes, dialogues, and images—is saved in neatly organized folders. This makes it easy for users to access the generated content for further customization or sharing.

## Pipeline Limitations

While the image generation functionality is part of ComicCrafter, the complete pipeline to automatically generate images in every scenario has not been fully implemented due to hardware limitations. The image generation aspect requires substantial computational resources, which may not be available on all systems. As a result, although the framework and integration with **ComicDiffusion** are present, users may need to manually run image generation for certain scenes, depending on their system's capabilities.

However, the **Mistral** model-driven story generation and scene breakdown are fully functional, providing users with automated storytelling capabilities. The integration with **ComicDiffusion** will be fully realized once the hardware requirements are met.

## How It Works

1. **Input**: You provide a story prompt that sets the theme, genre, and overall direction of the comic.
2. **Story Creation**: The prompt is processed by **Mistral** (or another LLM), which generates a story, including characters and plot development.
3. **Scene Division**: The tool then divides the story into scenes, separating dialogue and descriptions for each scene.
4. **Image Generation (Optional)**: While the tool can structure the scenes for you, the image generation feature requires manual activation due to hardware constraints. You can run **ComicDiffusion** to generate the corresponding images for each scene.
5. **Output**: The generated story, along with any images, is saved in organized folders for easy access and further use.

## Conclusion

ComicCrafter is an excellent tool for anyone looking to create comic-style stories automatically. While there are some current hardware limitations for fully automated image generation, the story and scene generation features are ready for creative use. The future of this tool will include a more efficient image generation pipeline once the necessary hardware resources are available.

