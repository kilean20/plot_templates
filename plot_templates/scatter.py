import matplotlib as matplt
import matplotlib.pyplot as plt
import seaborn as sns

    
def multivariateGrid(col_x, col_y, df, group_by, group_order, k_is_color=False, 
                     height = 4, xlim=None, ylim=None, scatter_kwargs={'alpha':0.5}): 
    
    def colored_scatter(x, y, c=None):
        def scatter(*args, **kwargs):
            args = (x, y)
            if c is not None:
                kwargs['c'] = c
            kwargs.update(scatter_kwargs)
            plt.scatter(*args, **kwargs)

        return scatter

    g = sns.JointGrid(
        x=col_x,
        y=col_y,
        data=df,
        height = height,
        xlim = xlim,
        ylim = ylim,
    )
    color = None
    legends=[]
    df_groupby = df.groupby(group_by)
    for group in group_order:
        df_group = df_groupby.get_group(group)
        legends.append(group)
        if k_is_color:
            color=name
        g.plot_joint(
            colored_scatter(df_group[col_x],df_group[col_y],color),
        )
        sns.distplot(
            df_group[col_x].values,
            ax=g.ax_marg_x,
            color=color,
        )
        sns.distplot(
            df_group[col_y].values,
            ax=g.ax_marg_y,
            color=color,            
            vertical=True
        )
    # Do also global Hist:
    sns.distplot(
        df[col_x].values,
        ax=g.ax_marg_x,
        color='grey'
    )
    sns.distplot(
        df[col_y].values.ravel(),
        ax=g.ax_marg_y,
        color='grey',
        vertical=True
    )
    legend = plt.legend(legends)
    
    return g, legend