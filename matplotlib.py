# import
import matplotlib.pyplot as plt
# Plot Officer Deshaun's hours_worked vs. day_of_week
plt.plot(deshaun.day_of_week, deshaun.hours_worked)
# Display Deshaun's plot
plt.show()

# Plot II, exploratory plots. 
plt.plot(deshaun.day_of_week, deshaun.hours_worked)
plt.plot(aditya.day_of_week, aditya.hours_worked)
plt.plot(mengfei.day_of_week, mengfei.hours_worked)

# Display all three line plots
plt.show()


#plot
plt.plot(six_months.month, six_months.hours_worked)
# Add annotation "Missing June data" at (2.5, 80)
plt.text(2.5, 80, "Missing June data")
# Display graph
plt.show()

# Change the color of Phoenix to `"DarkCyan"`
plt.plot(data["Year"], data["Phoenix Police Dept"],
   label="Phoenix", color="DarkCyan")
# Make the Los Angeles line dotted
plt.plot(data["Year"], data["Los Angeles Police Dept"],
   label="Los Angeles", linestyle=':')
# Add square markers to Philedelphia
plt.plot(data["Year"], data["Philadelphia Police Dept"],
   label="Philadelphia", marker='s')
# Add a legend
plt.legend()
# Display the plot
plt.show()

# Change the style to fivethirtyeight
plt.style.use("fivethirtyeight")
# Plot lines
plt.plot(data["Year"], data["Phoenix Police Dept"], label="Phoenix")
plt.plot(data["Year"], data["Los Angeles Police Dept"], label="Los Angeles")
plt.plot(data["Year"], data["Philadelphia Police Dept"], label="Philadelphia")
# Add a legend
plt.legend()
# Display the plot
plt.show()

#ggplot
plt.style.use("ggplot")
# Plot lines
plt.plot(data["Year"], 
   data["Phoenix Police Dept"], label="Phoenix")
plt.plot(data["Year"], 
   data["Los Angeles Police Dept"], label="Los Angeles")
plt.plot(data["Year"], 
   data["Philadelphia Police Dept"], label="Philadelphia")
# Add a legend
plt.legend()
# Display the plot
plt.show()

#style
plt.style.use("seaborn")
# Plot lines
plt.plot(data["Year"], 
   data["Phoenix Police Dept"], label="Phoenix")
plt.plot(data["Year"], 
   data["Los Angeles Police Dept"], label="Los Angeles")
plt.plot(data["Year"], 
   data["Philadelphia Police Dept"], label="Philadelphia")
# Add a legend
plt.legend()
# Display the plot
plt.show()

# 
plt.plot(ransom.letter, ransom.frequency,
         label="Ransom",
         linestyle=':', color='gray')
plt.show()

# Plot each line
plt.plot(ransom.letter, ransom.frequency,
         label='Ransom', linestyle=':', color='gray')

# X-values should be suspect1.letter
# Y-values should be suspect1.frequency
# Label should be "Fred Frequentist"
plt.plot(suspect1.letter, suspect1.frequency, label='Fred Frequentist')
plt.show()

