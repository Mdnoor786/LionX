# corona virus stats for LionX
from covid import Covid

from . import covidindia, eod, eor, lionx

plugin_type = "extra"


@lionx.lion_cmd(
    pattern="covid(?:\s|$)([\s\S]*)",
    command=("covid", plugin_type),
    info={
        "header": "To get latest information about covid-19.",
        "description": "Get information about covid-19 data in the given country/state(only Indian States).",
        "usage": "{tr}covid <state_name/country_name>",
        "examples": ["{tr}covid andhra pradesh", "{tr}covid india", "{tr}covid world"],
    },
)
async def corona(event):
    "To get latest information about covid-19."
    input_str = event.pattern_match.group(1)
    country = (input_str).title() if input_str else "World"
    lionxevent = await eor(event, "`Collecting data...`")
    covid = Covid(source="worldometers")
    try:
        country_data = covid.get_status_by_country_name(country)
    except ValueError:
        country_data = ""
    if country_data:
        hmm1 = country_data["confirmed"] + country_data["new_cases"]
        hmm2 = country_data["deaths"] + country_data["new_deaths"]
        data = ""
        data += f"\n⚠️ Confirmed   : <code>{hmm1}</code>"
        data += f"\n😔 Active           : <code>{country_data['active']}</code>"
        data += f"\n⚰️ Deaths         : <code>{hmm2}</code>"
        data += f"\n🤕 Critical          : <code>{country_data['critical']}</code>"
        data += f"\n😊 Recovered   : <code>{country_data['recovered']}</code>"
        data += f"\n💉 Total tests    : <code>{country_data['total_tests']}</code>"
        data += f"\n🥺 New Cases   : <code>{country_data['new_cases']}</code>"
        data += f"\n😟 New Deaths : <code>{country_data['new_deaths']}</code>"
        await lionxevent.edit(
            "<b>Corona Virus Info of {}:\n{}</b>".format(country, data),
            parse_mode="html",
        )
    else:
        data = await covidindia(country)
        if data:
            swt1 = int(data["new_positive"]) - int(data["positive"])
            swt2 = int(data["new_death"]) - int(data["death"])
            swt3 = int(data["new_cured"]) - int(data["cured"])
            result = f"<b>Corona virus info of {data['state_name']}\
                \n\n⚠️ Confirmed   : <code>{data['new_positive']}</code>\
                \n😔 Active           : <code>{data['new_active']}</code>\
                \n⚰️ Deaths         : <code>{data['new_death']}</code>\
                \n😊 Recovered   : <code>{data['new_cured']}</code>\
                \n🥺 New Cases   : <code>{swt1}</code>\
                \n😟 New Deaths : <code>{swt2}</code>\
                \n😃 New cured  : <code>{swt3}</code> </b>"
            await lionxevent.edit(result, parse_mode="html")
        else:
            await eod(
                lionxevent,
                "`Corona Virus Info of {} is not avaiable or unable to fetch`".format(
                    country
                ),
                5,
            )
