# CLAUDE CODE - HƯỚNG DẪN PHÁT TRIỂN AI (TEMPLATE TỔNG QUÁT)

> **Phiên bản**: 2.0 - Modular Architecture  
> **Template**: Áp dụng cho mọi dự án AI  
> **Tác giả**: [ntd237] | [ntd237.work@gmail.com] | [[GitHub](https://github.com/ntd237)]

---

## 📚 GIỚI THIỆU

File này là **core directive template** cho Claude Code Agent, có thể áp dụng cho **MỌI** dự án AI. 

Các prompt chi tiết được tổ chức theo module trong thư mục `.factory/prompts/`.

---

## 🎯 THÔNG TIN DỰ ÁN: [TÊN DỰ ÁN CỦA BẠN]

> **Hướng dẫn**: Chỉnh sửa section này để phù hợp với dự án cụ thể của bạn

### Tổng Quan
**[Tên Dự Án]** là [mô tả ngắn gọn về dự án - 1-2 câu].

**Ví dụ**:
- "Hệ thống nhận diện khuôn mặt real-time cho hệ thống chấm công"
- "Chatbot AI hỗ trợ khách hàng sử dụng LLM và RAG"
- "Platform phân tích dữ liệu tự động với AI Agents"

### Vấn Đề Giải Quyết
[Liệt kê 3-5 vấn đề chính mà dự án giải quyết]

**Template**:
- [Vấn đề 1]: [Mô tả]
- [Vấn đề 2]: [Mô tả]
- [Vấn đề 3]: [Mô tả]

**Ví dụ cho dự án CV**:
- Chấm công thủ công mất thời gian và dễ sai sót
- Khó kiểm soát giờ vào/ra của nhân viên
- Không có báo cáo tự động về attendance

### Giải Pháp
[Liệt kê các giải pháp/features chính]

**Template**:
- **[Feature 1]**: [Mô tả ngắn gọn]
- **[Feature 2]**: [Mô tả ngắn gọn]
- **[Feature 3]**: [Mô tả ngắn gọn]

**Ví dụ cho dự án NLP**:
- **Tự động phân loại**: Phân loại câu hỏi khách hàng theo category
- **Smart Response**: Đề xuất câu trả lời phù hợp từ knowledge base
- **Multi-language**: Hỗ trợ tiếng Việt, Anh, Trung

### Tech Stack
[Điều chỉnh theo dự án của bạn]

**Template cơ bản**:
- **Python**: 3.10+
- **Framework chính**: [PyTorch/TensorFlow/Scikit-learn/LangChain/...]
- **UI**: [PyQt5/Gradio/Streamlit/FastAPI/...]
- **Database**: [PostgreSQL/MongoDB/Redis/...] (nếu có)
- **LLM/Model**: [GPT/Claude/LLaMA/BERT/YOLO/...] (nếu có)
- **Other**: [Thư viện quan trọng khác]

**Ví dụ cho các loại dự án**:

<details>
<summary>📸 Computer Vision Project</summary>

```yaml
Python: 3.10+
Framework: PyTorch / TensorFlow
UI: PyQt5 (Desktop) hoặc Gradio (Web)
Model: YOLOv8, ResNet, EfficientNet
Libraries: OpenCV, albumentations
Hardware: CUDA-enabled GPU
```
</details>

<details>
<summary>💬 NLP/LLM Project</summary>

```yaml
Python: 3.10+
Framework: LangChain, HuggingFace Transformers
LLM: GPT-4, Claude, Llama 2
UI: Gradio, Streamlit
Vector DB: Pinecone, ChromaDB, FAISS
Libraries: sentence-transformers, tiktoken
```
</details>

<details>
<summary>🤖 AI Agents Project</summary>

```yaml
Python: 3.10+
Framework: LangChain, AutoGen, CrewAI
LLM: GPT-4, Claude Sonnet
UI: Gradio / FastAPI
Tools: WebSearch, Calculator, CodeExecutor
Memory: Redis, PostgreSQL
```
</details>

<details>
<summary>🎨 Generative AI Project</summary>

```yaml
Python: 3.10+
Framework: Diffusers, Stable Diffusion, DALL-E
UI: Gradio
Model: Stable Diffusion XL, ControlNet
Libraries: PIL, transformers
Hardware: High-end GPU (RTX 3090+)
```
</details>

### Cấu Trúc Dự Án
[Mô tả cấu trúc dự án của bạn]

**Template**:
```
project_name/
├── src/
│   ├── [module1]/           # [Mô tả module]
│   ├── [module2]/           # [Mô tả module]
│   ├── data/                # Data loaders & processors
│   ├── models/              # AI models
│   ├── ui/                  # User interface
│   └── utils/               # Utilities
├── resources/
│   ├── data/                # Raw/processed data
│   ├── configs/             # ⭐ YAML configs
│   ├── models/              # Pretrained models
│   └── prompts/             # Prompt templates (cho LLM)
├── .factory/prompts/        # ⭐ Claude Code prompts
├── tests/                   # Unit & integration tests
├── scripts/                 # Automation scripts
├── main.py                  # Entry point
└── requirements.txt         # Dependencies
```

---

## 📋 HỆ THỐNG PROMPTS MODULAR

### 🗂️ Cấu Trúc Prompts

Tất cả prompts được lưu trong `.factory/prompts/`:

```
.factory/prompts/
├── README.md                      # Hướng dẫn chi tiết
├── 01_general_guidelines.md       # ⭐ Nguyên tắc cốt lõi (luôn áp dụng)
├── 02_project_overview.md         # Xây dựng dự án từ đầu
├── 03_add_feature.md              # Thêm tính năng mới
├── 04_create_tool.md              # Tạo công cụ độc lập
├── 05_debug_fix.md                # Debug và sửa lỗi
├── 06_optimization.md             # Tối ưu hóa hiệu suất
├── 07_code_explanation.md         # ⭐ Giải thích logic code & kiến trúc (với Mermaid)
├── 08_ui_design.md                # ⭐ Thiết kế giao diện web/desktop
└── 09_readme_management.md        # ⭐ Tạo và cập nhật README
```

### 📖 Cách Sử Dụng

**Bước 1**: Luôn đọc `01_general_guidelines.md` TRƯỚC TIÊN

**Bước 2**: Chọn prompt phù hợp với tác vụ:

| Tác Vụ | Prompt | File |
|--------|--------|------|
| "Tạo dự án AI mới" | Project Overview | `02_project_overview.md` |
| "Thêm tính năng X" | Add Feature | `03_add_feature.md` |
| "Tạo tool CLI/GUI" | Create Tool | `04_create_tool.md` |
| "Fix lỗi Y" | Debug & Fix | `05_debug_fix.md` |
| "Tối ưu hóa Z" | Optimization | `06_optimization.md` |
| "Giải thích code/kiến trúc" | Code Explanation | `07_code_explanation.md` |
| "Thiết kế UI/UX" | UI Design | `08_ui_design.md` |
| "Tạo/Cập nhật README" | README Management | `09_readme_management.md` |

**Bước 3**: Tham khảo `.factory/prompts/README.md` cho hướng dẫn chi tiết

---

## ⚙️ QUY TẮC CẤU HÌNH

### TUYỆT ĐỐI KHÔNG HARDCODE

**✅ ĐÚNG**:
```python
# resources/configs/config.yaml
model:
  name: "resnet50"
  batch_size: 32
  learning_rate: 0.001

# src/models/trainer.py
import yaml
config = yaml.safe_load(open('resources/configs/config.yaml'))
batch_size = config['model']['batch_size']  # ✅ Load từ config
```

**❌ SAI**:
```python
batch_size = 32  # ❌ HARDCODE!
learning_rate = 0.001  # ❌ HARDCODE!
```

### Quy Tắc Config
- ✅ Tất cả tham số từ file YAML trong `resources/configs/`
- ✅ Tham số mới → Thêm vào YAML tương ứng
- ✅ Load lúc runtime, không compile-time
- ❌ **TUYỆT ĐỐI KHÔNG** hardcode trong code

### Tổ Chức Config Files

```
resources/configs/
├── config.yaml              # Cấu hình chính
├── model_config.yaml        # Cấu hình model
├── data_config.yaml         # Cấu hình data pipeline
├── training_config.yaml     # Cấu hình training
└── logging_config.yaml      # Cấu hình logging
```

---

## 🚀 QUY TRÌNH WORKFLOW CHUẨN

### Preliminary Tasks
1. 🔍 **Read/Grep/Glob**: Hiểu codebase hiện tại
2. 📚 **Git log** (optional): Tìm changes tương tự
3. 👁️ **Read chi tiết**: Xác định phạm vi ảnh hưởng
4. 📋 **TodoWrite**: Lập kế hoạch chi tiết (tasks ~15-20 phút)

### Implementation Rules
1. 🔍 **Lấy Context**: Luôn Read trước khi Edit
2. ✏️ **Chỉnh sửa**: Edit một logic nhỏ mỗi lần
3. ✅ **Kiểm thử**: Execute test NGAY sau mỗi edit
4. 💾 **Tôn trọng Codebase**: Không edit package files thủ công

### Package Management
```bash
# Python
pip install <package>
poetry add <package>

# JavaScript
npm install <package>
yarn add <package>

# Rust
cargo add <package>

# Go
go get <package>
```

---

## 💻 TIÊU CHUẨN CHẤT LƯỢNG

### Code Quality
- ✅ Python **3.10+**, tuân thủ **PEP 8**
- ✅ **100%** comments bằng tiếng Việt
- ✅ **Test coverage >90%**
- ✅ Type hints đầy đủ (Python 3.10+ style)
- ✅ Error handling toàn diện
- ✅ Docstrings đầy đủ (Google style)

### Documentation
- ✅ README.md bằng tiếng Việt
- ✅ Comments giải thích "**WHY**", không phải "HOW"
- ✅ API documentation (nếu có API)
- ✅ Inline documentation cho logic phức tạp

### Testing
- ✅ Unit tests cho core logic
- ✅ Integration tests cho components
- ✅ E2E tests cho key workflows
- ✅ Performance benchmarks

---

## 🎯 QUY TẮC CÔNG NGHỆ THEO LOẠI DỰ ÁN

### 📸 Computer Vision Projects
- ✅ **BẮT BUỘC** sử dụng **PyQt5** cho desktop UI
- ✅ **BẮT BUỘC** sử dụng **QThread** để quản lý threading
- ✅ Đảm bảo real-time performance (FPS >30)
- ✅ Ngăn UI đóng băng

### 💬 NLP/LLM Projects
- ✅ **Khuyến nghị** dùng **Gradio** hoặc **Streamlit** cho web UI
- ✅ **Khuyến nghị** dùng **FastAPI** cho REST API
- ✅ Implement caching cho LLM responses
- ✅ Handle rate limits và retries

### 🤖 AI Agents Projects
- ✅ Tách biệt **agents**, **tools**, **orchestration**
- ✅ Implement memory system (short-term + long-term)
- ✅ Logging chi tiết cho debugging
- ✅ Graceful error handling

### 🎨 Generative AI Projects
- ✅ Progress bars cho generation tasks
- ✅ Queue system cho batch processing
- ✅ Resource management (GPU memory)
- ✅ Result caching

---

## 📞 LIÊN HỆ

> **Hướng dẫn**: Cập nhật thông tin của bạn

- **Tác giả**: ntd237
- **Email**: ntd237.work@gmail.com
- **GitHub**: https://github.com/ntd237

---

## 🔗 THAM KHẢO NHANH

### 🆘 Khi Cần Giúp Đỡ
1. Đọc `.factory/prompts/README.md` - Hướng dẫn toàn diện
2. Chọn prompt phù hợp từ bảng trên
3. Tuân thủ `01_general_guidelines.md` cho mọi tác vụ

### 📊 Workflow Type
- **Build từ đầu** → `02_project_overview.md`
- **Mở rộng hiện tại** → `03_add_feature.md`
- **Tool riêng lẻ** → `04_create_tool.md`
- **Có lỗi** → `05_debug_fix.md`
- **Cần nhanh hơn** → `06_optimization.md`
- **Giải thích code/kiến trúc** → `07_code_explanation.md`
- **Thiết kế UI/UX** → `08_ui_design.md`
- **Tạo/Cập nhật README** → `09_readme_management.md`

---

## 🎓 HƯỚNG DẪN SETUP CHO DỰ ÁN MỚI

### Bước 1: Copy Template

```bash
# Copy FACTORY.md thành CLAUDE.md cho dự án mới
cp FACTORY.md your_new_project/CLAUDE.md

# Copy thư mục prompts
cp -r .factory your_new_project/
```

### Bước 2: Customize CLAUDE.md

Chỉnh sửa các sections sau trong `CLAUDE.md`:

1. **Header**:
   - Cập nhật tác giả, email, GitHub

2. **THÔNG TIN DỰ ÁN**:
   - Tên dự án
   - Vấn đề giải quyết
   - Giải pháp
   - Tech stack
   - Cấu trúc dự án

3. **QUY TẮC CÔNG NGHỆ**:
   - Chọn section phù hợp với loại dự án (CV/NLP/Agents/GenAI)

4. **LIÊN HỆ**:
   - Thông tin của bạn

### Bước 3: Setup Project Structure

```bash
# Tạo cấu trúc chuẩn
mkdir -p src/{data,models,ui,utils}
mkdir -p resources/{data,configs,models,prompts}
mkdir -p tests scripts

# Tạo config files
touch resources/configs/config.yaml
touch resources/configs/model_config.yaml

# Tạo requirements.txt
touch requirements.txt

# Tạo main.py
touch main.py
```

### Bước 4: Initialize Git

```bash
git init
git add .
git commit -m "Initial commit with FACTORY template"
```

---

## 📝 CHECKLIST DỰ ÁN MỚI

Khi bắt đầu dự án mới với template này:

### Setup
- [ ] Copy `FACTORY.md` → `CLAUDE.md`
- [ ] Copy `.factory/prompts/`
- [ ] Customize `CLAUDE.md` cho dự án cụ thể
- [ ] Tạo cấu trúc thư mục chuẩn
- [ ] Setup git repository

### Configuration
- [ ] Tạo các file YAML configs
- [ ] Setup `.env.example` và `.env`
- [ ] Cấu hình `.gitignore`

### Documentation
- [ ] Viết `README.md` chi tiết
- [ ] Document API (nếu có)
- [ ] Tạo example usage

### Quality
- [ ] Setup linting (pylint, flake8)
- [ ] Setup formatting (black, isort)
- [ ] Setup pre-commit hooks
- [ ] Setup CI/CD (GitHub Actions, GitLab CI)

---

## 🌟 BEST PRACTICES

### 1. Keep It Simple
- Code đơn giản > Code phức tạp
- Giải quyết vấn đề hiện tại, không over-engineer

### 2. Document Everything
- README toàn diện
- Comments giải thích "why"
- Docstrings đầy đủ

### 3. Test Thoroughly
- Unit tests cho functions
- Integration tests cho flows
- E2E tests cho workflows

### 4. Config Everything
- Không hardcode
- Tất cả vào YAML
- Environment variables cho secrets

### 5. Follow Patterns
- Consistent code style
- Reuse existing patterns
- DRY (Don't Repeat Yourself)

---

## 📚 TÀI LIỆU THAM KHẢO

### Python Best Practices
- [PEP 8](https://pep8.org/) - Style Guide
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [Real Python](https://realpython.com/)

### AI/ML Resources
- [PyTorch Docs](https://pytorch.org/docs/)
- [TensorFlow Docs](https://tensorflow.org/)
- [HuggingFace Docs](https://huggingface.co/docs)
- [LangChain Docs](https://python.langchain.com/)

### Tools
- [Black](https://black.readthedocs.io/) - Code Formatter
- [Pylint](https://pylint.org/) - Code Linter
- [pytest](https://pytest.org/) - Testing Framework

---

**Happy Coding with Claude Code! 🚀**

---

**Template này được thiết kế để áp dụng cho mọi dự án AI. Customize theo nhu cầu cụ thể của bạn!**
