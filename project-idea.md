# Mini-Project: Automated First-Time PC Setup

## 1. Overview

The idea is to build a system that automates the initial software setup of a new Windows PC.

The project will have **two main components**:

1. **A web application** — allows users to select the software they want installed.
2. **A desktop installer application** — converts the selected software list into an automated installation package that can be downloaded and executed on a PC.

The primary goal is to eliminate the repetitive process of manually downloading and installing multiple applications on every new computer.

---

## 2. Problem Statement

Setting up a large number of new computers can be time-consuming and repetitive.

For example, when a college sets up a new computer laboratory with 50–100 PCs, every machine may need the same set of applications:

* Google Chrome
* Visual Studio Code
* VMware
* Git
* C/C++ development tools
* Python
* Java
* Other required utilities and software

Normally, an administrator would have to download and install these applications individually on every machine, repeatedly going through installation wizards and configuration steps.

This project aims to automate that process.

---

## 3. Proposed Solution

We will develop a website where the administrator can select the applications required for a particular PC or environment.

After selecting the applications, the website will generate a customized installer package.

The administrator can then download the package as an executable installer, such as:

* `.exe`
* Potentially `.msi` for supported deployment scenarios

When the generated installer is executed on a new PC, it will:

1. Identify the selected applications.
2. Download the required installers from their official sources.
3. Run the installations automatically.
4. Handle installation parameters where possible.
5. Install the applications without requiring the user to repeatedly click through installation wizards.
6. Provide a final status indicating which applications were successfully installed and which failed.

---

## 4. Example Use Case

### College Computer Laboratory

A college receives **50 new computers** for a programming laboratory.

The administrator visits our website and selects:

* Google Chrome
* Visual Studio Code
* Git
* Python
* Java
* C/C++ development tools
* VMware

The website generates a customized installation package.

The administrator downloads the package and runs it on each computer.

Instead of manually installing every application, the package automatically downloads and installs the selected software.

This significantly reduces the time and effort required to prepare the laboratory.

---

## 5. Project Architecture

### Part 1 — Web Application

The website will provide:

* Application catalogue
* Application search
* Categories
* Application descriptions
* Version information
* Software selection
* Selected application list
* Installer/package generation
* Download of the generated installer

Potential categories could include:

* Development
* Browsers
* Productivity
* Virtualization
* Education
* Utilities
* Media
* Networking

The website should ideally obtain application installers and metadata from **official sources** rather than hosting third-party installers ourselves.

---

### Part 2 — Automated Installer

The generated application will act as the automation layer.

A possible workflow would be:

**Generated Installer → Python Automation → Download Software → Silent Installation → Verify Installation → Report Results**

The Python component could maintain information such as:

```text
Application
├── Name
├── Version
├── Download URL
├── Installer Type
├── Installation Arguments
├── Installation Detection Method
└── Dependencies
```

For example:

```text
VS Code
Download: Official Microsoft URL
Installer: .exe
Arguments: /VERYSILENT
Detection: Check installation path / registry
```

The automation script would then use the appropriate installation method for each application.

---

## 6. Important Technical Considerations

There are several areas we should investigate during development:

### Silent Installation

Not every application supports the same silent-installation parameters.

We will need an application database containing the appropriate installation commands and arguments for supported software.

### Administrator Privileges

Some applications require administrator permissions.

The installer should handle elevation appropriately.

### Software Sources

Applications should preferably be downloaded from official vendor sources.

We should avoid hosting copyrighted installers ourselves unless we have permission to do so.

### Version Management

We need to determine how application versions will be handled.

Possible approaches:

* Always install the latest version.
* Allow the administrator to select a specific version.
* Maintain a database of supported versions.

### Installation Verification

After installation, the system should verify whether the application was successfully installed.

For example:

```text
Chrome       ✓ Installed
VS Code      ✓ Installed
Python       ✓ Installed
VMware       ✗ Installation failed
```

### Failure Handling

If one application fails, the installer should ideally continue installing the remaining applications rather than stopping completely.

At the end, the user should receive a summary of successful and failed installations.

---

## 7. Potential Future Features

Once the basic version works, the project could be extended with:

* Custom software bundles
* Presets such as "Programming Lab", "Office PC", or "Design Lab"
* Automatic dependency installation
* Version selection
* Installation logs
* Offline installation packages
* Network deployment to multiple PCs
* Centralized administration
* PC configuration beyond software installation
* Hardware/OS compatibility checks
* Automatic software updates
* Enterprise deployment support

---

## 8. Initial MVP

For the first version, we should keep the scope relatively small.

### Website

* Application catalogue
* Search and categories
* Application selection
* Generate installer
* Download installer

### Installer

* Run with administrator privileges
* Download selected applications
* Perform silent installations
* Track installation status
* Display final installation report

A small set of applications can be supported initially, such as:

* Google Chrome
* Visual Studio Code
* Git
* Python
* 7-Zip
* Java

Once the core system works reliably, we can expand the application catalogue and deployment capabilities.

---

## 9. Core Objective

The main objective of the project is to create a **"one-click first setup" system for Windows PCs**.

Instead of:

**Download → Install → Next → Next → Finish → Repeat**

the desired experience is:

**Select Applications → Generate Installer → Run Installer → PC Ready**

The project can initially target individual users and small organizations, with the potential to evolve into a larger PC provisioning and software deployment platform.
