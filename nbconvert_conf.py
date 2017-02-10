c = get_config()

#Export all the notebooks in the current directory to the sphinx_howto format.
c.NbConvertApp.notebooks = ['ipy/*.ipynb']
c.NbConvertApp.export_format = 'markdown'
c.FilesWriter.build_directory = 'content'
c.TemplateExporter.template_file = 'templates/markdown.tpl'
c.NbConvertApp.output_files_dir = 'images/{notebook_name}_files'
