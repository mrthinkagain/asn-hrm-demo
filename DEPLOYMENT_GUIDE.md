# 🚀 ASN Technologies HRMS - Deployment Guide

## 📦 Current Setup

- **Repository**: https://github.com/mrthinkagain/asn-hrm-demo
- **Database**: Supabase (PostgreSQL)
- **Deployment**: Fly.io (recommended)

## 🗄️ Database Configuration

Your database is hosted on Supabase. To connect:

1. Get your connection string from Supabase dashboard:
   - Go to: Project Settings → Database
   - Copy the "Connection pooling" URI

2. The connection string format:
   ```
   postgres://postgres:[PASSWORD]@db.xxxxx.supabase.co:6543/postgres
   ```

## 🌐 Deploy to Fly.io

### Prerequisites
- Fly.io account: https://fly.io (free)
- Fly CLI installed

### Steps:

1. **Install Fly CLI** (if not installed):
   ```bash
   powershell -Command "iwr https://fly.io/install.ps1 -useb | iex"
   ```

2. **Login to Fly.io**:
   ```bash
   fly auth login
   ```

3. **Initialize Fly.io in your project**:
   ```bash
   fly launch
   ```
   - It will ask to connect to GitHub repo
   - It will detect `fly.toml` and `Dockerfile`

4. **Set environment variables**:
   ```bash
   fly secrets set DATABASE_URL="postgres://postgres:[YOUR-PASSWORD]@db.bcwariuktdyhdrajycka.supabase.co:6543/postgres"
   fly secrets set SECRET_KEY="your-django-secret-key"
   fly secrets set DEBUG=False
   fly secrets set ALLOWED_HOSTS="your-app-name.fly.dev"
   ```

5. **Deploy**:
   ```bash
   fly deploy
   ```

6. **Get your app URL**:
   ```bash
   fly open
   ```

## 📝 Environment Variables Needed

Create these in Fly.io dashboard or via CLI:

- `DATABASE_URL` - Supabase PostgreSQL connection string
- `SECRET_KEY` - Django secret key
- `DEBUG` - Set to `False` for production
- `ALLOWED_HOSTS` - Your domain (e.g., `asn-technologies-hrms.fly.dev`)

## 🎯 After Deployment

1. Access your app at: `https://your-app-name.fly.dev`
2. Create superuser: `fly ssh console -C "python manage.py createsuperuser"`
3. Login and start using!

## 💡 Login Credentials

**Local Testing** (http://127.0.0.1:8000):
- Username: `ramteja`
- Email: `ramtejach5@gmail.com`
- Password: Check local configuration

**Production** (after deployment):
- Create admin user via: `fly ssh console`
- Or use Django admin to create users

---

## 🔒 Security Notes

- Never commit passwords or secrets to GitHub
- Use Fly.io secrets for sensitive environment variables
- Keep database connection string secure

## 📞 Support

For issues or questions, refer to:
- Horilla documentation: https://github.com/horilla/horilla
- Fly.io docs: https://fly.io/docs
- Supabase docs: https://supabase.com/docs

