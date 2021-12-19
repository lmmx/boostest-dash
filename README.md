# boostest

Dash app using UK Coronavirus Data Dashboard API records to display figures for booster jabs, LFD tests, and PCR tests

- `sample_data.csv` was downloaded from [this URL](https://api.coronavirus.data.gov.uk/v2/data?areaType=overview&metric=cumVaccinationFirstDoseUptakeByPublishDatePercentage&metric=cumVaccinationSecondDoseUptakeByPublishDatePercentage&metric=cumVaccinationThirdInjectionUptakeByPublishDatePercentage&metric=newPCRTestsByPublishDate&metric=newLFDTestsBySpecimenDate&format=csv)
  on 19/12/2021
- Adapted from [`dash_simple_example_pandas_datareader.py`](https://gist.github.com/chriddyp/3d2454905d8f01886d651f207e2419f0) in the [dash app samples](https://pypi.org/project/dash/)
