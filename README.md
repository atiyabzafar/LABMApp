# Language Evolution Through Immigration Dynamics - Interactive Application

## 🌍 Overview

This folder contains interactive applications for exploring **Language Evolution Through Immigration Dynamics** using agent-based modeling. Choose between:

1. **Streamlit Web App** (Recommended for sharing) - `streamlit_app.py`
2. **Tkinter Desktop App** - `gui_app.py`

## 🚀 Quick Start

### Option 1: Streamlit Web App (Easiest to Share!)

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run streamlit_app.py
```

The app will open in your browser at `http://localhost:8501`

### Option 2: Tkinter Desktop App

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python3 gui_app.py
```

A desktop window will open.

## 📤 Sharing Your App

### Method 1: Streamlit Cloud (FREE & EASIEST!) ⭐

**Best for:** Public sharing, no installation required for users

1. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Add language evolution application"
   git push
   ```

2. **Deploy on Streamlit Cloud:**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository
   - Set main file: `streamlit_app.py`
   - Click "Deploy"

3. **Share the URL:**
   - You'll get a URL like: `https://yourapp.streamlit.app`
   - Anyone can access it without installation!

**Advantages:**
- ✅ FREE hosting
- ✅ No installation for users
- ✅ Automatic updates when you push to GitHub
- ✅ Works on any device (desktop, tablet, mobile)
- ✅ Professional URL

### Method 2: Hugging Face Spaces (FREE)

**Best for:** ML/AI community, academic sharing

1. Create account at [huggingface.co](https://huggingface.co)
2. Create new Space (select Streamlit)
3. Upload files or connect GitHub
4. Get URL like: `https://huggingface.co/spaces/username/appname`

### Method 3: GitHub + Instructions

**Best for:** Technical users, open source projects

1. Push to GitHub
2. Users clone and run locally:
   ```bash
   git clone https://github.com/yourusername/language-evolution-app
   cd language-evolution-app
   pip install -r requirements.txt
   streamlit run streamlit_app.py
   ```

### Method 4: Docker Container

**Best for:** Reproducibility, enterprise deployment

Create `Dockerfile`:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "streamlit_app.py"]
```

Build and run:
```bash
docker build -t language-evolution .
docker run -p 8501:8501 language-evolution
```

### Method 5: Executable (Desktop App)

**Best for:** Non-technical users, offline use

Convert Tkinter app to executable:
```bash
pip install pyinstaller
pyinstaller --onefile --windowed gui_app.py
```

Share the executable file from `dist/` folder.

## 📊 Comparison of Sharing Methods

| Method | Ease of Sharing | User Installation | Cost | Best For |
|--------|----------------|-------------------|------|----------|
| **Streamlit Cloud** | ⭐⭐⭐⭐⭐ | None | FREE | Public sharing |
| **Hugging Face** | ⭐⭐⭐⭐ | None | FREE | Academic/ML |
| **GitHub** | ⭐⭐⭐ | Required | FREE | Developers |
| **Docker** | ⭐⭐⭐ | Docker only | FREE | Enterprise |
| **Executable** | ⭐⭐⭐⭐ | None | FREE | Desktop users |

## 🎯 Recommended: Streamlit Cloud

**Why Streamlit is best for your use case:**

1. **Zero installation for users** - Just share a link
2. **Works everywhere** - Desktop, mobile, tablet
3. **Free hosting** - No costs
4. **Auto-updates** - Push to GitHub, app updates automatically
5. **Professional** - Clean URL, looks polished
6. **Fast deployment** - 5 minutes from code to live app

## 📁 Files in This Folder

```
Language Evolution App/
├── streamlit_app.py          # Web app (RECOMMENDED)
├── gui_app.py                 # Desktop app
├── agents.py                  # Agent classes
├── districts.py               # Spatial structure
├── model.py                   # Simulation engine
├── visualization.py           # Plotting functions
├── requirements.txt           # Dependencies
├── README.md                  # This file
├── GUI_README.md              # Detailed Tkinter GUI docs
├── QUICK_START_GUI.md         # Quick reference
└── GUI_COMPLETE_SUMMARY.md    # Full summary
```

## 🔧 Local Development

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit App Locally

```bash
streamlit run streamlit_app.py
```

### Run Tkinter App Locally

```bash
python3 gui_app.py
```

## 🌐 Example Deployment

### Streamlit Cloud Deployment Steps

1. **Prepare Repository:**
   ```bash
   cd "Language Evolution App"
   git init
   git add .
   git commit -m "Initial commit"
   ```

2. **Push to GitHub:**
   ```bash
   # Create repo on GitHub first, then:
   git remote add origin https://github.com/yourusername/language-evolution-app.git
   git push -u origin main
   ```

3. **Deploy:**
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Repository: `yourusername/language-evolution-app`
   - Branch: `main`
   - Main file path: `streamlit_app.py`
   - Click "Deploy"

4. **Share:**
   - Copy your app URL
   - Share with anyone!

## 💡 Tips for Sharing

### For Academic Papers
Add to your paper:
> "An interactive web application is available at: https://yourapp.streamlit.app"

### For Presentations
- Show live demo during presentation
- QR code to app URL
- Audience can try it on their phones

### For Teaching
- Students can explore without installation
- Works on university computers
- Mobile-friendly for homework

### For Collaborators
- Share URL via email
- No setup instructions needed
- Everyone sees same interface

## 🆘 Troubleshooting

### Streamlit App Won't Start Locally

```bash
# Check Streamlit installation
streamlit --version

# Reinstall if needed
pip install --upgrade streamlit
```

### Deployment Fails on Streamlit Cloud

- Check `requirements.txt` is in root
- Ensure all imports are listed
- Check file paths are relative
- Review deployment logs

### App is Slow

- Reduce default simulation years
- Add caching with `@st.cache_data`
- Optimize model code

## 📚 Documentation

- **Streamlit Docs:** [docs.streamlit.io](https://docs.streamlit.io)
- **Deployment Guide:** [docs.streamlit.io/streamlit-community-cloud](https://docs.streamlit.io/streamlit-community-cloud)
- **Tkinter GUI Docs:** See `GUI_README.md`

## 🎓 Educational Use

### For Students
- No installation barriers
- Works on any device
- Intuitive interface
- Immediate feedback

### For Instructors
- Share one link with class
- No IT support needed
- Track usage (Streamlit analytics)
- Easy to update

### For Researchers
- Share with collaborators globally
- Reproducible results
- Export data for analysis
- Professional presentation

## 🚀 Next Steps

1. **Try locally:** `streamlit run streamlit_app.py`
2. **Push to GitHub:** Commit all files
3. **Deploy to Streamlit Cloud:** 5-minute setup
4. **Share your URL:** With colleagues, students, reviewers

## 📧 Support

For issues or questions:
- Check documentation files in this folder
- Review Streamlit documentation
- Check GitHub issues

---

**Ready to share your research with the world!** 🌍✨

**Recommended:** Deploy on Streamlit Cloud for easiest sharing!
