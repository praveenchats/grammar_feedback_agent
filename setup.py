from setuptools import setup, find_packages

setup(
    name="nw18-grammar-feedback-agent",  # Updated name with org prefix
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "openai==1.43.0",
        "python-dotenv==1.0.1",
        "httpx==0.27.0",
    ],
    author="Praveen Kumar",
    author_email="your.email@organization.com",
    description="A package for grammar analysis using Azure OpenAI.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/praveenchats/grammar_feedback_agent",  # Update to your org's repo
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Private :: Do Not Upload",  # Prevents accidental upload to public PyPI
    ],
    python_requires=">=3.8",
)