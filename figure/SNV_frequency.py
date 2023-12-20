#this code can be used directly after parsing the vcf file, the code is specfically for SARS-CoV-2, can be modify based on specific virus
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import os

def SNV_frequency_plot_multi(csv_file_paths, file_names, hamster_title):
    """
    Read multiple CSV files into DataFrames and plot POS against ALT_FREQ multiplied by 100
    in a format suitable for Nature publication.

    Parameters:
        csv_file_paths (list of str): The file paths to the CSV files.
        file_names (list of str): The names of the files to be displayed as the plot legend.

    Returns:
        None: The function produces a plot.
    """
    # Configure Matplotlib for Nature-style plots
    sns.set_context("paper", font_scale=2)
    sns.set_style("white")

    fig, ax = plt.subplots(figsize=(16, 4), dpi=300)
    colors = ['#415262', '#E63946', '#F4A261', '#2A9D8F']  # Unique colors for each CSV
    
    legend_patches = []
    
    for i, (csv_file_path, file_name) in enumerate(zip(csv_file_paths, file_names)):
        # Step 1: Read the CSV file into a DataFrame
        df = pd.read_csv(csv_file_path)
        
        # Step 2: Check if 'POS' and 'ALT_FREQ' columns exist
        if 'POS' not in df.columns or 'ALT_FREQ' not in df.columns:
            raise ValueError(f"Required columns 'POS' and 'ALT_FREQ' are not present in the CSV file {csv_file_path}.")

        # Step 3: Calculate ALT_FREQ * 100
        df['ALT_FREQ_100'] = df['ALT_FREQ'] * 100

        # Step 4: Generate the plot
        sns.scatterplot(x='POS', y='ALT_FREQ_100', data=df, alpha=0.7, color=colors[i], edgecolors='black', zorder=10)

        # Create legend patches
        legend_patches.append(mpatches.Patch(color=colors[i], label=file_name))
    
    # Add gene segments and other plot elements
    ax.axvspan(0, 21555, facecolor='#C5C5C9', alpha=0.3, zorder=1) # ORF1a|b
    ax.axvspan(21563, 25384, facecolor='#3BC6C8', alpha=0.3, zorder=1) # Spike
    ax.axvspan(26245, 26472, facecolor='#83c54a', alpha=0.3, zorder=1) # Envelope
    ax.axvspan(25393, 26220, facecolor='#C5C5C9', alpha=0.3, zorder=1) # ORF3a
    ax.axvspan(26523, 27191, facecolor='#e68329', alpha=0.3, zorder=1) # Matrix
    ax.axvspan(28274, 29533, facecolor='#a41020', alpha=0.3, zorder=1) # Nucleocapsid
    ax.axvspan(27202, 28259, facecolor='#C5C5C9', alpha=0.3, zorder=1) # ORF 6-8
    ax.axvspan(29558, 29674, facecolor='#C5C5C9', alpha=0.3, zorder=1) # ORF 10

    # Add gene segments names slightly above the graph
    max_val = df['ALT_FREQ_100'].max() + 8  # Slightly above the maximum value
    plt.text(10777, max_val, 'ORF1a|b', fontweight='bold', size=14, ha='center', rotation=0)
    plt.text(23473, max_val, 'S', fontweight='bold', size=14, ha='center', rotation=0)
    plt.text(25806, max_val, 'ORF3a', fontweight='bold', size=8, ha='center', rotation= 90)
    plt.text(26358, max_val, 'E', fontweight='bold', size=8, ha='center', rotation=0)
    plt.text(26857, max_val, 'M', fontweight='bold', size=8, ha='center', rotation=0) 
    
    plt.text(28903, max_val, 'N', fontweight='bold', size=8, ha='center', rotation=0)
    plt.text(27730, max_val, 'ORF6|7|8', fontweight='bold', size=8, ha='center', rotation=90)
    plt.text(29616, max_val, 'ORF10', fontweight='bold', size=8, ha='center', rotation=90)

    # Add legend
    plt.legend(handles=legend_patches, loc='upper left', bbox_to_anchor=(1, 1), fontsize='medium')

    # Remaining plotting code
    ax.set_title(hamster_title, fontsize=24, pad=40)  # pad moves the title above
    
    # Set axis labels
    ax.set_xlabel('SARS-CoV-2 Genome Position', fontsize=20)
    ax.set_ylabel('SNV Frequency %', fontsize=20)
    
    # Remove grid background
    ax.grid(False)
    
    # Add dotted line at y=20
    plt.axhline(y=5, linestyle='--', linewidth=1, color='gray')
    
    plt.tight_layout(rect=[0,0,0.85,1])  # Adjust layout to fit legend outside
    output_file_path = hamster_title+"_cleaning"+'/'+hamster_title+"_combined_SNV_plot"
    plt.savefig(output_file_path, dpi=600, bbox_inches='tight')  # Save before showing the plot
#     os.makedirs(hamster_title, exist_ok=True)
#     plt.savefig(hamster_title+"/"+hamster_title+"_combined.pdf", dpi=600, bbox_inches='tight') 
    plt.show()  # This should be after saving




