# Punt Return Risk Analysis

**⚠️ Work in Progress**: This project is ongoing. More comprehensive analysis and insights are being developed.

Data analysis of NFL punts challenging the value of punt returns. This project quantifies the risks and rewards of punt returns to assess if they are strategically worthwhile or unnecessarily risky and "silly."

## Overview

This project analyzes NFL punt plays from the 2009-2019 seasons to evaluate whether punt returns provide genuine strategic value or if they introduce unnecessary risk without commensurate benefit. The analysis combines Python data processing with statistical analysis in JASP to explore punt return outcomes and their impact on field position and game momentum. The project also includes comparative filtering scripts for pass and run plays to contextualize punt return data within the broader offensive landscape.

**Status**: This is an ongoing passion project. Initial analyses have been completed, but deeper investigation into field position value, risk-reward ratios, and situational factors is underway.

## Data Source

The punt data used in this project is sourced from the **nflscrapR** public dataset maintained by Ryan Yurko:

- **Repository**: [nflscrapR-data](https://github.com/ryurko/nflscrapR-data/tree/master)
- **Data Coverage**: NFL play-by-play data from 2009-2019 seasons (regular season and postseason)
- **Attribution**: All raw data files are sourced from the nflscrapR repository. Please refer to the original repository for data documentation and licensing.

**Note**: The raw data files are not included in this repository due to their large size. Users can download them directly from the source repository using the scripts provided.

## Project Structure

```
punt-return-analysis/
├── README.md
├── combineNFLData.py           # Combines regular and postseason data files
├── puntplaysonly.py            # Filters combined data for punt plays only
├── passplaysonly.py            # Filters combined data for pass plays (comparison)
├── runplaysonly.py             # Filters combined data for run plays (comparison)
├── JASP_punt_analysis.pdf      # Statistical analysis results from JASP
└── data/                        # (Not included - download from source)
    ├── reg_pbp_2009.csv
    ├── post_pbp_2009.csv
    └── ...
```

## Code Overview

### `combineNFLData.py`

This script combines NFL play-by-play data from multiple seasons into a single dataset.

**Features:**
- Loops through years 2009-2019
- Loads both regular season (`reg_pbp_YYYY.csv`) and postseason (`post_pbp_YYYY.csv`) files
- Combines all files into a single CSV: `nfl_pbp_2009_2019_combined.csv`
- Provides status updates for each file loaded

**Usage:**
```bash
python combineNFLData.py
```

**Requirements:**
- pandas
- Data files downloaded from nflscrapR repository in the specified folder path

### `puntplaysonly.py`

This script filters the combined dataset to include only punt plays.

**Features:**
- Loads the combined play-by-play dataset
- Filters for plays where `play_type == 'punt'`
- Outputs filtered data to: `nfl_pbp_2009_2019_punts_only.csv`

**Usage:**
```bash
python puntplaysonly.py
```

### `passplaysonly.py`

This script filters the combined dataset to include only pass plays for comparative analysis.

**Features:**
- Loads the combined play-by-play dataset
- Filters for plays where `play_type == 'pass'`
- Outputs filtered data to: `nfl_pbp_2009_2019_pass_only.csv`

**Usage:**
```bash
python passplaysonly.py
```

### `runplaysonly.py`

This script filters the combined dataset to include only run plays for comparative analysis.

**Features:**
- Loads the combined play-by-play dataset
- Filters for plays where `play_type == 'run'`
- Outputs filtered data to: `nfl_pbp_2009_2019_run_only.csv`

**Usage:**
```bash
python runplaysonly.py
```

**Note**: The pass and run play filters are used to provide context for punt return outcomes and to compare field position dynamics across different play types.

## Analysis Method

Statistical and exploratory analyses were conducted using **[JASP](https://jasp-stats.org/)**, an open-source statistical software package. The JASP analysis file is included as `JASP_punt_analysis.pdf`, which contains:

- Descriptive statistics of punt return outcomes
- Hypothesis testing for punt return effectiveness
- Initial visualizations and summary statistics
- Comparative analysis across play types (in development)

## Getting Started

1. **Clone this repository:**
   ```bash
   git clone https://github.com/yourusername/punt-return-analysis.git
   cd punt-return-analysis
   ```

2. **Download the data:**
   - Visit [nflscrapR-data repository](https://github.com/ryurko/nflscrapR-data/tree/master)
   - Download the regular season and postseason CSV files for years 2009-2019
   - Place them in a folder (e.g., `data/` or update the path in the scripts)

3. **Install dependencies:**
   ```bash
   pip install pandas
   ```

4. **Run the scripts:**
   ```bash
   python combineNFLData.py
   python puntplaysonly.py
   python passplaysonly.py
   python runplaysonly.py
   ```

5. **Analyze the data:**
   - Open the filtered datasets in JASP or your preferred statistical software
   - Review `JASP_punt_analysis.pdf` for the current analysis

## Key Research Questions

This project aims to answer:
- Are punt returns worth the risk of turnovers and penalties?
- How do punt return outcomes compare to fair catch scenarios?
- What is the expected value (field position gain/loss) of attempting a punt return?
- Do punt returns provide meaningful strategic advantage, or are they "silly"?
- How do punt play dynamics differ from pass and run plays?

## Future Work

- **Expand statistical analysis**: Deeper hypothesis testing and confidence intervals
- **Field position modeling**: Quantify expected field position value for different punt return outcomes
- **Risk-reward analysis**: Calculate optimal punt return decision thresholds
- **More recent seasons**: Include 2020-2024 NFL seasons
- **Player-specific metrics**: Incorporate returner skill level and performance variance
- **Situational analysis**: Examine game context (score, time, field position) impact on punt return strategy
- **Coaching comparison**: Analyze team-specific punt return strategies and their effectiveness

## About

This is a passion project aimed at providing insights into special teams strategy by quantitatively exploring punt return effectiveness and associated risks. The project was developed to challenge conventional football wisdom and provide data-driven perspectives on special teams decision-making.

## Contributing

Feedback, suggestions, and collaboration are welcome! Feel free to open an issue or submit a pull request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- **nflscrapR Team**: Thank you to Ryan Yurko and contributors for maintaining the nflscrapR dataset
- **JASP Team**: For providing accessible open-source statistical software
