# LinkExtractorFitGirl_repackPicker

# MultiHost Direct Link Extractor

A powerful Python-based tool that extracts direct downloadable links from multiple file hosting services such as Datanodes and FuckingFast. The tool automatically resolves protected file-host pages into direct CDN download URLs compatible with IDM and other download managers.

---

## Features

* Extracts direct download links from:

  * Datanodes
  * FuckingFast
* Automatically bypasses basic host-page protection
* Saves all resolved direct links into output files
* IDM-compatible direct links
* Batch processing support
* Automatically removes processed links from `input.txt`
* Colored console logs and progress tracking
* Lightweight and easy to use

---

## Prerequisites

Ensure you have the following installed before running the script:

* Python 3.8+

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

### 1. Add Host Links

Paste all supported host links into:

```text
input.txt
```

One link per line.

Example:

```text
https://datanodes.to/xxxxx/file.part01.rar
https://fuckingfast.co/view/xxxxx
```

---

### 2. Run The Script

```bash
python main.py
```

---

### 3. What The Script Does

The script will:

* Process every link from `input.txt`
* Extract the real direct CDN download link
* Save extracted links into:

```text
output_links_<timestamp>.txt
```

* Remove processed links from `input.txt`

---

## IDM Batch Download

You can directly import the generated output file into IDM:

### IDM Import Steps

1. Open IDM
2. Go to:

   * Tasks
   * Import
   * From Text File
3. Select:

```text
output_links_<timestamp>.txt
```

4. Start batch download

---

## Supported Hosts

| Host        | Status    |
| ----------- | --------- |
| Datanodes   | Supported |
| FuckingFast | Supported |

More hosts may be added in future updates.

---

## Output Example

```text
https://dl123.datanodes.to/d/xxxxx/file.part01.rar
https://dl5.fuckingfast.co/dl/xxxxx
```

---

## Disclaimer

This project is created for educational and research purposes only.

The developer is not responsible for:

* misuse of the software
* copyright violations
* illegal distribution of content

Users are responsible for complying with the laws and regulations applicable in their country.
