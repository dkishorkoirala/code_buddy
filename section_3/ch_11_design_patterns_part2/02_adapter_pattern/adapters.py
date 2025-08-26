from interfaces import DataProcessor, DataVisualizer
from legacy_system import LegacyDataAnalyzer, LegacyChartGenerator


class LegacyDataAnalyzerAdapter(DataProcessor):
    """Adapter for LegacyDataAnalyzer to work with the DataProcessor interface."""

    def __init__(self):
        # TODO: Initialize the adapter with a LegacyDataAnalyzer instance
        # TODO: Create self.legacy_analyzer as a LegacyDataAnalyzer object
        self.legacy_analyzer = LegacyDataAnalyzer()

    def process_data(self, data):
        """Process data using the legacy analyzer."""
        # TODO: Implement data validation to ensure data is a list
        # TODO: Validate that all items in data are numeric (int or float)
        # TODO: Raise ValueError with appropriate message if validation fails
        # TODO: Use legacy_analyzer.load_data() to load the data
        # TODO: Use legacy_analyzer.run_analysis() to process the data
        # TODO: Return True on successful processing
        if not all(isinstance(item, (int, float)) for item in data):
            raise ValueError("Data must be a list of numeric values")

        self.legacy_analyzer.load_data(data)
        self.legacy_analyzer.run_analysis()
        return True

    def get_results(self):
        """Get results from the legacy analyzer."""
        # TODO: Use legacy_analyzer.fetch_results() to get results
        # TODO: Return empty dictionary {} if results is None
        # TODO: Otherwise return the results as received
        if self.legacy_analyzer.fetch_results() is None:
            return {}
        return self.legacy_analyzer.fetch_results()


class LegacyChartGeneratorAdapter(DataVisualizer):
    """Adapter for LegacyChartGenerator to work with the DataVisualizer interface."""

    def __init__(self, chart_type="bar"):
        # TODO: Initialize the adapter with a LegacyChartGenerator instance
        # TODO: Set self.legacy_chart_generator to the instance
        # TODO: Set self.chart_type to the given chart type
        # TODO: Use legacy_chart_generator.initialize_chart() to set the chart type
        self.legacy_chart_generator = LegacyChartGenerator()
        self.chart_type = chart_type
        self.legacy_chart_generator.initialize_chart(chart_type)

    def visualize(self, data):
        """Create visualization using the legacy chart generator."""
        # TODO: Implement data validation to ensure data is a list
        # TODO: Validate that all items in data are numeric (int or float)
        # TODO: Raise ValueError with appropriate message if validation fails
        # TODO: Use legacy_chart_generator.add_data_series() to add data
        # TODO: Use legacy_chart_generator.render() to create the chart
        # TODO: Return the success status from render()
        if not all(isinstance(item, (int, float)) for item in data):
            raise ValueError("Data must be a list of numeric values")

        self.legacy_chart_generator.add_data_series(data)
        return self.legacy_chart_generator.render()

    def export_visualization(self, filename):
        """Export the visualization to a file using the legacy chart generator."""
        # TODO: Check if filename ends with '.png', '.jpg', or '.pdf'
        # TODO: If no valid extension, append '.png' as default
        # TODO: Use legacy_chart_generator.save_chart() to save the file
        # TODO: Return the success status from save_chart()
        if not filename.endswith((".png", ".jpg", ".pdf")):
            filename += ".png"

        return self.legacy_chart_generator.save_chart(filename)
