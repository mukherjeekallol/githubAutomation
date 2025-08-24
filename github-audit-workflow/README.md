# GitHub Audit Workflow

This project implements a GitHub Actions workflow that generates an audit document whenever a pull request is created. The audit document contains information about the pull request creator and is saved to a file.

## Project Structure

```
github-audit-workflow
├── .github
│   └── workflows
│       └── audit.yml        # GitHub Actions workflow configuration
├── audit
│   └── create_audit.py      # Python script to create the audit document
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## Getting Started

To set up the GitHub Actions workflow and the audit script, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd github-audit-workflow
   ```

2. **Install dependencies**:
   Make sure you have Python installed, then install the required packages listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the GitHub Actions workflow**:
   The workflow is defined in `.github/workflows/audit.yml`. It is triggered on pull request events. You can customize the workflow as needed.

4. **Run the audit script**:
   The audit script can be executed manually or will run automatically when a pull request is created. To run it manually, use:
   ```bash
   python audit/create_audit.py
   ```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.