# 🚀 Deployment Guide - Streamlit Cloud

## Quick Deploy (5 Minutes!)

### Step 1: Prepare Your Repository

```bash
cd "GUI Application"

# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Add interactive GUI for migration ABM"
```

### Step 2: Push to GitHub

```bash
# Create a new repository on GitHub.com first
# Then connect and push:

git remote add origin https://github.com/YOUR_USERNAME/migration-abm-gui.git
git branch -M main
git push -u origin main
```

### Step 3: Deploy on Streamlit Cloud

1. **Go to:** [share.streamlit.io](https://share.streamlit.io)

2. **Sign in** with your GitHub account

3. **Click "New app"**

4. **Fill in the form:**
   - **Repository:** `YOUR_USERNAME/migration-abm-gui`
   - **Branch:** `main`
   - **Main file path:** `streamlit_app.py`
   - **App URL:** Choose a custom name (e.g., `migration-abm`)

5. **Click "Deploy"**

6. **Wait 2-3 minutes** for deployment

7. **Done!** Your app is live at: `https://YOUR_APP_NAME.streamlit.app`

## 🎉 You're Live!

Your app is now accessible to anyone with the URL. No installation required!

## 📤 Sharing Your App

### Share the URL

```
https://YOUR_APP_NAME.streamlit.app
```

### Add to Your Paper

```latex
An interactive web application for exploring the model is available at: 
\url{https://YOUR_APP_NAME.streamlit.app}
```

### Create a QR Code

1. Go to [qr-code-generator.com](https://www.qr-code-generator.com/)
2. Enter your app URL
3. Download QR code
4. Add to presentations/posters

### Social Media

```
🌍 Explore our Brazilian-Portuguese Migration ABM!

Interactive web app: https://YOUR_APP_NAME.streamlit.app

Adjust parameters, run simulations, visualize results - all in your browser!

#AgentBasedModeling #CulturalEvolution #DataScience
```

## 🔄 Updating Your App

### Make Changes

```bash
# Edit your code
nano streamlit_app.py

# Commit changes
git add .
git commit -m "Update: improved visualization"

# Push to GitHub
git push
```

**That's it!** Streamlit Cloud automatically redeploys your app within minutes.

## ⚙️ Advanced Configuration

### Custom Domain (Optional)

In Streamlit Cloud settings:
1. Go to app settings
2. Add custom domain
3. Update DNS records

### Secrets Management (If Needed)

For API keys or sensitive data:

1. In Streamlit Cloud, go to app settings
2. Click "Secrets"
3. Add secrets in TOML format:
   ```toml
   [secrets]
   api_key = "your_key_here"
   ```

4. Access in code:
   ```python
   import streamlit as st
   api_key = st.secrets["api_key"]
   ```

### Resource Limits

Free tier limits:
- **CPU:** 1 core
- **RAM:** 1 GB
- **Storage:** Unlimited (for code)
- **Apps:** Unlimited public apps

If you need more, upgrade to paid tier.

## 📊 Analytics

View app usage:
1. Go to Streamlit Cloud dashboard
2. Select your app
3. View analytics:
   - Number of visitors
   - Usage over time
   - Geographic distribution

## 🐛 Troubleshooting

### Deployment Fails

**Check:**
- `requirements.txt` exists and is correct
- All imports are listed in requirements
- File paths are relative (not absolute)
- No syntax errors in code

**View logs:**
- Click "Manage app" in Streamlit Cloud
- Check deployment logs
- Look for error messages

### App is Slow

**Solutions:**
- Add caching: `@st.cache_data`
- Reduce default parameters
- Optimize model code
- Consider paid tier for more resources

### App Crashes

**Common causes:**
- Memory limit exceeded (reduce population size)
- Timeout (reduce simulation years)
- Missing dependencies (check requirements.txt)

**Fix:**
- Add error handling
- Set reasonable default parameters
- Test locally first

## 🔒 Privacy & Security

### Public vs Private

- **Public apps** (free): Anyone with URL can access
- **Private apps** (paid): Require authentication

### Data Privacy

- No user data is stored by default
- Simulations run in isolated containers
- Each user gets fresh session

### Best Practices

- Don't hardcode sensitive data
- Use secrets for API keys
- Add disclaimer if needed
- Consider data privacy laws

## 💰 Costs

### Free Tier (Recommended)

- ✅ Unlimited public apps
- ✅ 1 GB RAM per app
- ✅ Community support
- ✅ Perfect for academic/research use

### Paid Tiers

If you need:
- Private apps
- More resources
- Priority support
- Custom domains

Pricing: Check [streamlit.io/cloud](https://streamlit.io/cloud)

## 📚 Additional Resources

### Documentation
- [Streamlit Docs](https://docs.streamlit.io)
- [Deployment Guide](https://docs.streamlit.io/streamlit-community-cloud)
- [API Reference](https://docs.streamlit.io/library/api-reference)

### Community
- [Forum](https://discuss.streamlit.io)
- [GitHub](https://github.com/streamlit/streamlit)
- [Twitter](https://twitter.com/streamlit)

### Examples
- [Gallery](https://streamlit.io/gallery)
- [Example Apps](https://github.com/streamlit/example-app-cv-model)

## ✅ Deployment Checklist

Before deploying:

- [ ] Code works locally
- [ ] `requirements.txt` is complete
- [ ] No hardcoded file paths
- [ ] Default parameters are reasonable
- [ ] Error handling is in place
- [ ] README is clear
- [ ] .gitignore excludes unnecessary files
- [ ] Repository is public (or you have private app plan)

After deploying:

- [ ] Test all features
- [ ] Check on different devices
- [ ] Share URL with test users
- [ ] Monitor for errors
- [ ] Update documentation with URL

## 🎯 Success Metrics

Track your app's impact:

- **Usage:** Number of visitors
- **Engagement:** Average session duration
- **Geography:** Where users are from
- **Feedback:** User comments/issues

## 🌟 Tips for Success

1. **Start simple:** Deploy basic version first
2. **Test thoroughly:** Try on different devices
3. **Get feedback:** Share with colleagues
4. **Iterate:** Update based on feedback
5. **Promote:** Share on social media, in papers
6. **Monitor:** Check analytics regularly
7. **Maintain:** Keep dependencies updated

## 📧 Support

Need help?

1. **Check logs** in Streamlit Cloud
2. **Search forum** at discuss.streamlit.io
3. **Review docs** at docs.streamlit.io
4. **Ask community** on forum or GitHub

## 🎊 You're Ready!

Follow the steps above and your app will be live in minutes!

**Your URL will be:** `https://YOUR_APP_NAME.streamlit.app`

Share it with the world! 🌍✨

---

**Questions?** Check the main README.md or Streamlit documentation.

**Happy deploying!** 🚀
