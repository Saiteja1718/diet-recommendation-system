# Hugging Face Spaces Deployment Guide

## 🚀 Deploy to Hugging Face Spaces

Hugging Face Spaces is the **best option** for this app because:
- ✅ **16GB RAM** (vs 1GB on Streamlit Cloud)
- ✅ **Optimized for ML models** like TinyLlama
- ✅ **Fast model loading**
- ✅ **Completely FREE**
- ✅ **Auto-deploys** from GitHub

---

## 📋 Prerequisites

1. **Hugging Face Account**
   - Sign up at https://huggingface.co/join
   - It's free!

2. **GitHub Repository**
   - Your code is already on GitHub: `Saiteja1718/diet-recommendation-system`

---

## 🎯 Deployment Steps

### Method 1: Direct Upload (Easiest)

1. **Go to Hugging Face Spaces**
   - Visit: https://huggingface.co/spaces
   - Click "Create new Space"

2. **Configure Your Space**
   - **Space name**: `diet-recommendation-system`
   - **License**: MIT
   - **SDK**: Streamlit
   - **Hardware**: CPU basic (free)
   - **Visibility**: Public

3. **Upload Files**
   - Click "Files" tab
   - Upload all files from your project
   - Make sure these key files are included:
     - `README_HF.md` (rename to `README.md`)
     - `app.py`
     - `requirements.txt`
     - `packages.txt`
     - All folders: `Streamlit_Frontend/`, `Data/`, `FastAPI_Backend/`

4. **Wait for Build**
   - Hugging Face will automatically build your app
   - First build takes 5-10 minutes (downloading TinyLlama model)
   - Watch the build logs in the "Logs" tab

5. **Access Your App**
   - URL: `https://huggingface.co/spaces/[your-username]/diet-recommendation-system`
   - Share this link with anyone!

---

### Method 2: GitHub Integration (Recommended)

1. **Create Space on Hugging Face**
   - Visit: https://huggingface.co/spaces
   - Click "Create new Space"
   - Configure as above

2. **Connect to GitHub**
   - In your Space settings, go to "Settings" → "Repository"
   - Click "Connect to GitHub"
   - Select your repository: `Saiteja1718/diet-recommendation-system`
   - Choose branch: `main`

3. **Auto-Deploy**
   - Every time you push to GitHub, Hugging Face automatically rebuilds
   - No manual uploads needed!

---

## 📁 Required Files (Already Created)

All these files are now in your repository:

### 1. `README_HF.md`
- Hugging Face Space configuration
- **Action**: Rename to `README.md` when uploading to HF Spaces

### 2. `app.py`
- Entry point for Hugging Face Spaces
- Launches Streamlit from correct directory
- Sets proper port (7860) for HF Spaces

### 3. `requirements.txt`
- All Python dependencies
- Includes torch, transformers, streamlit, etc.

### 4. `packages.txt`
- System-level dependencies (if needed)

---

## ⚙️ Configuration Details

### Hardware Requirements
- **Free tier**: CPU basic (16GB RAM, 2 vCPUs) ✅ **Sufficient**
- **Upgrade options**: 
  - CPU upgrade (32GB RAM) - $0.60/hour
  - GPU T4 - $0.60/hour (faster LLM inference)

### Environment Variables
No environment variables needed! Everything runs locally.

### Storage
- **Space storage**: 50GB (free)
- **Your app size**: ~5GB (torch + transformers + model)
- ✅ **Plenty of space**

---

## 🎨 Customization

### Update Space Metadata
Edit the header in `README_HF.md`:
```yaml
---
title: Diet Recommendation System
emoji: 🥗
colorFrom: purple
colorTo: pink
sdk: streamlit
sdk_version: 1.28.0
app_file: app.py
---
```

### Custom Domain (Optional)
- Available on paid plans
- Or use the free `huggingface.co/spaces/[username]/[space]` URL

---

## 🐛 Troubleshooting

### Build Fails
- Check "Logs" tab for errors
- Common issues:
  - Missing files: Upload all folders
  - Wrong Python version: Use Python 3.11
  - Dependency conflicts: Check requirements.txt

### App Crashes
- Check "Logs" tab for runtime errors
- Common issues:
  - Out of memory: Upgrade to CPU upgrade tier
  - Model download timeout: First load takes 5-10 min

### Slow Performance
- First load is slow (downloading TinyLlama)
- Subsequent loads are fast (model cached)
- Consider upgrading to GPU for faster inference

---

## 📊 Expected Performance

### First Load
- **Build time**: 5-10 minutes
- **Model download**: 2.2GB TinyLlama
- **Total setup**: ~10-15 minutes

### After First Load
- **App startup**: 10-20 seconds
- **Chat response**: 10-30 seconds
- **Page load**: Instant
- **Model**: Cached in memory

---

## 🔗 Useful Links

- **Your Space**: `https://huggingface.co/spaces/[username]/diet-recommendation-system`
- **HF Spaces Docs**: https://huggingface.co/docs/hub/spaces
- **Streamlit on HF**: https://huggingface.co/docs/hub/spaces-sdks-streamlit
- **Support**: https://discuss.huggingface.co/

---

## ✅ Deployment Checklist

Before deploying, make sure:

- [ ] All files committed to GitHub
- [ ] `README_HF.md` ready (will rename to README.md)
- [ ] `app.py` in root directory
- [ ] `requirements.txt` updated
- [ ] `packages.txt` created
- [ ] Hugging Face account created
- [ ] Space created on Hugging Face
- [ ] Files uploaded or GitHub connected
- [ ] Build successful
- [ ] App accessible via URL

---

## 🎉 After Deployment

Once deployed, you'll have:
- ✅ **Free hosting** with 16GB RAM
- ✅ **Public URL** to share
- ✅ **Auto-deploys** from GitHub
- ✅ **Fast LLM inference**
- ✅ **Professional appearance**

**Your app will be live at:**
`https://huggingface.co/spaces/[your-username]/diet-recommendation-system`

Share this link with anyone to showcase your Diet Recommendation System! 🚀
