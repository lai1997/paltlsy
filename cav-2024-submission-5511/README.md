# LTL Learning on GPUs

Welcome to the anonymous artefact repository for the CAV 2024 submission "LTL Learning on GPUs" (submission 5511). While the organisation of this artefact is currently in progress, we have gathered  all the necessary codes, scripts, and benchmarks for the convenience of our reviewers. A more structured version will be submitted for the main artefact review if we are invited for artefact evaluation.

Please feel free to explore the provided materials, which include:

- Main GPU code: `code/ltli6463.cu`
- Additional algorithms: `code/dc.py`
- Benchmarks: `benchmarks`

For those interested in running the work, you may utilize your Google account to access Colab. Open the provided `colab_notebook_scripts.ipynb` notebook, clone this repository there, and execute all scripts to ensure reproducibility. All the information regarding how to compile and run the GPU code using different inputs, plus all scripts for making the additional benchmarks, is available in the Colab Notebook. We have also separated the `masking.ipynb` notebook, as the last benchmark requires a different version of the GPU code and accompanying scripts.

Note: Upon opening your Colab Notebook, kindly verify your GPU connection by navigating to the "Runtime" tab, selecting "Change runtime type," and confirming the GPU as the hardware accelerator. Additionally, should you choose to upgrade to a paid version, you gain access to superior GPUs like V100 and A100, further enhancing your computing experience.