# Medical-Data-Visualizer
def draw_cat_plot():
    # Load the dataset
    df = pd.read_csv('medical_examination.csv')

    # Add overweight column
    df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

    # Normalize the data for cholesterol and glucose
    df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
    df['gluc'] = (df['gluc'] > 1).astype(int)

    # Clean the data
    df = df[(df['ap_lo'] <= df['ap_hi']) &
            (df['height'] >= df['height'].quantile(0.025)) &
            (df['height'] <= df['height'].quantile(0.975)) &
            (df['weight'] >= df['weight'].quantile(0.025)) &
            (df['weight'] <= df['weight'].quantile(0.975))]

    # Create a correlation matrix
    corr_matrix = df.corr()

    # Set up the matplotlib figure
    fig, axes = plt.subplots(figsize=(12, 10), nrows=1, ncols=2)

    # Plot the catplots for categorical features
    sns.catplot(x='variable', hue='value', col='cardio', data=pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active']), kind='count', ax=axes[0])
    axes[0].set_xticklabels(rotation=45)
    axes[0].set_xlabel('Variable')
    axes[0].set_ylabel('Total Count')
    axes[0].set_title('Categorical Features')

    # Plot the heatmap for the correlation matrix
    sns.heatmap(corr_matrix, annot=True, fmt='.1f', cmap='coolwarm', center=0, ax=axes[1], square=True, mask=corr_matrix.to_numpy() == 1)
    axes[1].set_title('Correlation Matrix')

    # Save the figure
    plt.savefig('output.png')

    return fig

