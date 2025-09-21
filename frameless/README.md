# 🚀 Frameless - AI-Powered Content Generation Platform

A modern FastAPI-based platform for generating and managing AI-powered content with image support.

## ✨ Features

### 🔥 **Newly Added Practical Features:**

- **Complete REST API** - Full CRUD operations for users, content, and images
- **AI Content Generation** - Generate stories and content based on themes and prompts
- **Image Upload & Management** - Upload, store, and manage images with descriptions
- **User Authentication** - JWT-based authentication system
- **Interactive Web Interface** - Beautiful HTML interface for easy API testing
- **File Upload Support** - Handle image uploads with proper validation
- **Database Integration** - PostgreSQL with SQLAlchemy ORM
- **Docker Support** - Complete containerization setup

### 📋 **API Endpoints:**

#### Authentication
- `POST /api/v1/auth/token` - Login and get access token
- `GET /api/v1/auth/me` - Get current user info

#### Users
- `POST /api/v1/users` - Create new user
- `GET /api/v1/users` - List all users
- `GET /api/v1/users/{id}` - Get user by ID
- `PUT /api/v1/users/{id}` - Update user
- `DELETE /api/v1/users/{id}` - Delete user

#### Content
- `POST /api/v1/content/generate` - Generate AI content
- `POST /api/v1/content` - Create content manually
- `GET /api/v1/content` - List content (with filtering)
- `GET /api/v1/content/{id}` - Get content by ID
- `PUT /api/v1/content/{id}` - Update content
- `DELETE /api/v1/content/{id}` - Delete content

#### Images
- `POST /api/v1/images/upload` - Upload image file
- `POST /api/v1/images` - Create image record
- `GET /api/v1/images` - List images (with filtering)
- `GET /api/v1/images/{id}` - Get image by ID
- `DELETE /api/v1/images/{id}` - Delete image

## 🚀 Quick Start

### Prerequisites
- Docker and Docker Compose
- Python 3.8+ (for local development)

### Using Docker (Recommended)

1. **Clone and navigate to the project:**
   ```bash
   git clone <your-repo-url>
   cd Frameless/frameless
   ```

2. **Set up environment variables:**
   ```bash
   export POSTGRES_SERVER=localhost
   export POSTGRES_USER=frameless_user
   export POSTGRES_PASSWORD=frameless_password
   export POSTGRES_DB=frameless_db
   export MODE=DEV
   ```

3. **Build and run with Docker Compose:**
   ```bash
   ./docker-compose.sh build frameless
   ./docker-compose.sh run --service-ports --rm frameless
   ```

4. **Access the application:**
   - **Web Interface:** http://localhost:8080
   - **API Documentation:** http://localhost:8080/docs
   - **API Base URL:** http://localhost:8080/api/v1

### Local Development Setup

1. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements/base.txt
   pip install -e .
   ```

3. **Set up PostgreSQL database:**
   ```bash
   docker run -p 5432:5432 -e POSTGRES_PASSWORD='mypassword' --rm -d --name db postgres:latest
   ```

4. **Set environment variables:**
   ```bash
   export POSTGRES_SERVER=localhost
   export POSTGRES_USER=postgres
   export POSTGRES_PASSWORD=mypassword
   export POSTGRES_DB=frameless_dev
   export MODE=DEV
   ```

5. **Run the application:**
   ```bash
   python frameless/main.py
   ```

## 🎯 Practical Use Cases

### 1. **Content Marketing Platform**
- Generate blog posts, social media content, and marketing copy
- Create themed content for different campaigns
- Manage content library with images and descriptions

### 2. **Storytelling Platform**
- Generate stories based on themes (adventure, romance, mystery, etc.)
- Create visual stories with multiple images and captions
- Share stories publicly or keep them private

### 3. **Educational Content Creator**
- Generate educational content for different subjects
- Create visual learning materials with images
- Organize content by themes and topics

### 4. **Social Media Management**
- Generate posts for different platforms
- Create image galleries with descriptions
- Schedule and manage content publication

### 5. **Creative Writing Assistant**
- Get AI assistance for creative writing projects
- Generate story ideas and prompts
- Create visual storyboards with images

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `MODE` | Environment mode (DEV/TEST/PROD) | DEV |
| `POSTGRES_SERVER` | Database server | localhost |
| `POSTGRES_USER` | Database username | - |
| `POSTGRES_PASSWORD` | Database password | - |
| `POSTGRES_DB` | Database name | - |
| `SECRET_KEY` | JWT secret key | Auto-generated |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token expiration | 11520 (8 days) |

### CORS Configuration
The API supports CORS for cross-origin requests. Configure allowed origins in your environment or settings.

## 📊 Database Schema

### Users Table
- `id` - Primary key
- `username` - Unique username
- `email` - Unique email address
- `password` - Plain text password (for reference)
- `hashed_password` - Bcrypt hashed password

### Generated Content Table
- `id` - Primary key
- `title` - Content title
- `content` - Main content text
- `theme` - Content theme/category
- `is_story` - Boolean flag for story type
- `is_public` - Public visibility flag
- `image_url_1/2/3` - URLs for associated images
- `caption_1/2/3` - Captions for images
- `created_at` - Creation timestamp
- `owner_id` - Foreign key to users table

### Images Table
- `id` - Primary key
- `url` - Image URL or file path
- `description` - Image description
- `is_public` - Public visibility flag
- `created_at` - Creation timestamp
- `owner_id` - Foreign key to users table

## 🧪 Testing

### Run Tests
```bash
# Using Docker
./docker-compose.sh run test_frameless

# Local testing
make test
```

### Test Coverage
The project includes comprehensive test coverage for:
- API endpoints
- Database models
- Authentication
- Services and utilities

## 📈 Future Enhancements

### Phase 1 (Immediate)
- [ ] Real OpenAI API integration
- [ ] Image processing and resizing
- [ ] Content scheduling
- [ ] User roles and permissions

### Phase 2 (Short-term)
- [ ] Social media integration
- [ ] Content analytics
- [ ] Export functionality (PDF, Word)
- [ ] Mobile app API optimization

### Phase 3 (Long-term)
- [ ] Team collaboration features
- [ ] Advanced AI models integration
- [ ] Content marketplace
- [ ] Multi-language support

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Maintainers

- **Faiza Jibril** - *Maintainer* - [jayasibi99@gmail.com](mailto:jayasibi99@gmail.com)

## 🆘 Support

For support and questions:
- Create an issue on GitHub
- Email: jayasibi99@gmail.com
- Check the API documentation at `/docs` endpoint

---

**Made with ❤️ using FastAPI, SQLAlchemy, and modern web technologies**
