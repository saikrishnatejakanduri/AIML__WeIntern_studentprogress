# Publish this project on GitHub (beginner guide)

1. Sign in to GitHub and choose **New repository**.
2. Name it `aiml-week1-student-success`. For an internship submission, a **Public** repository is convenient if WeIntern has not provided different privacy instructions.
3. Keep **Add a README** unchecked because this project already contains one.
4. Upload the project files and folders, or use Git locally.

## Git commands (if Git is installed)
Run these commands from the project root:

```bash
git init
git add .
git commit -m "Complete Week 1 student performance analysis"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/aiml-week1-student-success.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username and the remote URL with the repository URL shown by GitHub. Do not share passwords, tokens, or other credentials.

## Before submitting
- Open the notebook and use **Restart Kernel and Run All Cells**.
- Check that `outputs/charts/` and the report open correctly.
- Review the repository in browser view.
- Submit your actual GitHub URL in the WeIntern portal; a repository link has not been created automatically by this project package.
