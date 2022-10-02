import args from "args";

args
	.option(
		"from",
		"The start date for the data in YYYY-MM-DD format, e.g. 1999-10-31"
	)
	.option(
		"to",
		"The end date for the data in YYYY-MM-DD format, e.g. 1999-11-25",
		new Date().toISOString().split("T")[0]
	)
	.option(
		"duration",
		"The duration of the data to be scraped in years, starting from today, e.g. 30",
		10
	)
	.option(
		"step",
		"Frequency of data scraping in months, e.g. 12 (for yearly data)",
		12
	)
	.option("output", "The output file path", "output.csv");

const flags = args.parse(process.argv);

const { from, to, duration, step, output } = flags;

if (from && to) {
	console.log("Scraping from", from, "to", to, "with step", step);
} else if (duration) {
	console.log("Scraping for", duration, "years with step", step);
} else {
	console.log("No valid arguments provided");
}

console.log(flags);
